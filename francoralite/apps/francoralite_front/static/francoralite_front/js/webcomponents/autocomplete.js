"use strict";
/* jslint node: true */
/* jshint esversion: 6 */
/* globals customElements */


class FrancoraliteAutocomplete extends HTMLElement {

    constructor() {
        super();

        const componentName = this.getAttribute('name');

        this.setAttribute('class', 'francoralite-autocomplete-webcomponent');

        this.inputField = document.createElement('input');
        this.inputField.setAttribute('id', this.getAttribute('data-id') || componentName);
        this.inputField.setAttribute('type', 'text');
        this.inputField.setAttribute('class', 'input');
        this.appendChild(this.inputField);

        this.proposalsList = document.createElement('ul');
        this.proposalsList.setAttribute('class', 'proposals');
        this.appendChild(this.proposalsList);

        const operator = this.getOperator();
        if (operator && operator.name) {
            this.classList.add('with-operator');

            this.operatorCheckedText = operator['checked-label'];
            this.operatorUncheckedText = operator.label || 'operator';

            this.operatorCheckbox = document.createElement('input');
            this.operatorCheckbox.setAttribute('id', componentName + '_operator');
            this.operatorCheckbox.setAttribute('type', 'checkbox');
            this.operatorCheckbox.setAttribute('class', 'operator');
            this.operatorCheckbox.setAttribute('name', operator.name);
            this.operatorCheckbox.setAttribute('value', componentName);
            this.operatorCheckbox.setAttribute('title', operator.tooltip || '');
            this.appendChild(this.operatorCheckbox);

            this.operatorLabel = document.createElement('label');
            this.operatorLabel.setAttribute('for', componentName + '_operator');
            this.operatorLabel.setAttribute('class', 'operator-label');
            this.operatorLabel.setAttribute('title', operator.tooltip || '');
            this.operatorLabel.innerHTML = this.operatorUncheckedText;
            this.appendChild(this.operatorLabel);
        }

        JSON.parse(this.getAttribute('data-values') || '[]').forEach(
            item => this.addSelectedItem(item[0], item[1], item[2], item[3])
        );
    }

    connectedCallback() {
        this.inputField.addEventListener('keyup', (event) => this.inputChanged(event));
        this.inputField.addEventListener('focus', () => this.inputChanged());
        this.inputField.addEventListener('blur', () => window.setTimeout(() => this.showProposals([]), 200));

        this.proposalsList.addEventListener('click', (event) => this.proposalClick(event));

        if (this.operatorCheckedText) {
            this.operatorCheckbox.addEventListener('change', (event) => {
                this.operatorLabel.innerHTML = event.target.checked ?
                    this.operatorCheckedText : this.operatorUncheckedText;
            });
        }

        this.addEventListener('click', (event) => {
            if (event.target === this) {
                this.inputField.focus();
            }
        });
    }

    getOperator() {
        const defaultOperator = this.getDefaultOperator() || {};
        return {
            'name': this.getAttribute('data-operator-name') || defaultOperator.name,
            'label': this.getAttribute('data-operator-label') || defaultOperator.label,
            'checked-label': this.getAttribute('data-operator-checked-label') || defaultOperator['checked-label'],
            'tooltip': this.getAttribute('data-operator-tooltip') || defaultOperator.tooltip
        };
    }

    getDefaultOperator() {
        return {
            'name': 'or_operators',
            'label': 'et',
            'checked-label': 'ou',
            'tooltip': 'cochez la case pour changer l’opérateur de requêtage'
        };
    }

    getUrl() {
        return this.getAttribute('data-url') || this.getDefaultUrl();
    }

    getDefaultUrl() {
        return null;
    }

    inputChanged(event) {
        const text = this.inputField.value;
        if (text && text.length >= 1) {
            const xhr = new XMLHttpRequest();
            xhr.addEventListener('load', (event) => {
                const data = JSON.parse(event.target.response);
                this.showProposals(data.results !== undefined ? data.results : data);
            });
            xhr.open('GET', this.getUrl() + text, true);
            xhr.send(null);
        }
    }

    showProposals(items) {
        this.proposalsList.innerHTML = '';
        items.forEach(item => {
            const data = this.parseProposal(item);
            const li = document.createElement('li');
            li.innerHTML = data.label + (data.url ? ' (<a href="' + data.url + '">afficher</a>)' : '');
            li.setAttribute('class', 'proposal');
            li.setAttribute('title', data.tooltip || '');
            li.setAttribute('data-label', data.label || '');
            li.setAttribute('data-tooltip', data.tooltip || '');
            li.setAttribute('data-url', data.url || '');
            li.setAttribute('data-value', data.value || '');
            this.proposalsList.appendChild(li);
        });
    }

    parseProposal(item) {
        return {
            'value': item.email,
            'label': item.name.title + ' ' + item.name.first + ' ' + item.name.last,
            'url': 'mailto:' + item.email,
            'tooltip': item.email
        };
    }

    proposalClick(event) {
        if (event.target instanceof HTMLLIElement) {
            this.addSelectedItem(
                event.target.getAttribute('data-value'),
                event.target.getAttribute('data-label'),
                event.target.getAttribute('data-url'),
                event.target.getAttribute('data-tooltip')
            );
            this.showProposals([]);
            this.inputField.value = '';
            this.inputField.focus();
        }
    }

    addSelectedItem(value, label, url, tooltip) {
        if (! label) {
            label = value;
        }

        const span = document.createElement('span');
        span.setAttribute('class', 'item');
        span.setAttribute('title', tooltip || '');
        span.innerHTML = url ? '<a href="' + url + '">' + label + '</a>' : label;
        this.insertBefore(span, this.inputField);

        const input = document.createElement('input');
        input.setAttribute('type', 'hidden');
        input.setAttribute('name', this.getAttribute('name'));
        input.setAttribute('value', value);
        span.appendChild(input);

        const button = document.createElement('button');
        button.innerHTML = '&times;';
        button.setAttribute('class', 'remove');
        button.setAttribute('title', 'supprimer cet élément');
        button.addEventListener('click', function(event) {
            span.parentNode.removeChild(span);
        });
        span.appendChild(button);
    }
}

class FrancoraliteAuthorities extends FrancoraliteAutocomplete {
    parseProposal(item) {
        return {
            'value': item.id,
            'label': item.first_name + ' ' + item.last_name,
            'url': '/authority/' + item.id,
            'tooltip': null
        };
    }
}

class FrancoraliteInformers extends FrancoraliteAuthorities {
    getDefaultUrl() {
        return '/api/authority?limit=10&is_informer=true&ordering=first_name+last_name&search=';
    }
}

class FrancoraliteCollectors extends FrancoraliteAuthorities {
    getDefaultUrl() {
        return '/api/authority?limit=10&is_collector=true&ordering=first_name+last_name&search=';
    }
}

class FrancoraliteLocations extends FrancoraliteAutocomplete {
    getDefaultUrl() {
        return '/api/locationgis?limit=10&ordering=code&search=';
    }

    parseProposal(item) {
        return {
            'value': item.id,
            'label': item.name,
            'url': '/location_gis/' + item.id,
            'tooltip': null
        };
    }
}

class FrancoraliteDances extends FrancoraliteAutocomplete {
    getDefaultUrl() {
        return '/api/dance?limit=10&&search=';
    }

    parseProposal(item) {
        return {
            'value': item.id,
            'label': item.name,
            'url': null,
            'tooltip': null
        };
    }
}

customElements.define('francoralite-autocomplete', FrancoraliteAutocomplete);
customElements.define('francoralite-informers', FrancoraliteInformers);
customElements.define('francoralite-collectors', FrancoraliteCollectors);
customElements.define('francoralite-locations', FrancoraliteLocations);
customElements.define('francoralite-dances', FrancoraliteDances);
