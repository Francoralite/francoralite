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

        const operators = this.getOperators();
        if (operators) {
            this.classList.add('with-operators');

            const operatorsDiv = document.createElement('div');
            operatorsDiv.setAttribute('class', 'operators');
            this.appendChild(operatorsDiv);

            operators.forEach(operator => {
                const operatorInput = document.createElement('input');
                operatorInput.setAttribute('id', componentName + '_operator_' + operator.value);
                operatorInput.setAttribute('type', 'radio');
                operatorInput.setAttribute('class', 'operator');
                operatorInput.setAttribute('name', componentName + '_operator');
                operatorInput.setAttribute('value', operator.value);
                operatorInput.setAttribute('title', operator.tooltip || '');
                operatorsDiv.appendChild(operatorInput);

                const operatorLabel = document.createElement('label');
                operatorLabel.setAttribute('for', componentName + '_operator_' + operator.value);
                operatorLabel.setAttribute('class', 'operator-label');
                operatorLabel.setAttribute('title', operator.tooltip || '');
                operatorLabel.innerHTML = operator.label || '';
                operatorsDiv.appendChild(operatorLabel);
            });
        }

        JSON.parse(this.getAttribute('data-values') || '[]').forEach(
            item => this.addSelectedItem(this.parseProposal(item))
        );
    }

    connectedCallback() {
        this.inputField.addEventListener('keyup', (event) => this.inputChanged(event));
        this.inputField.addEventListener('focus', () => this.inputChanged());
        this.inputField.addEventListener('blur', () => window.setTimeout(() => this.clearInputAndProposals(), 200));

        this.proposalsList.addEventListener('click', (event) => this.proposalClick(event));

        const defaultOperator = this.getAttribute('data-default-operator');
        let operatorFound = false;
        this.querySelectorAll('.operator').forEach(operator => {
            if (defaultOperator === operator.value) {
                operator.checked = true;
                operatorFound = true;
            }
        });
        if (! operatorFound) {
            this.querySelector('.operator').checked = true;
        }

        this.addEventListener('click', (event) => {
            if (event.target === this) {
                this.inputField.focus();
            }
        });
    }

    getOperators() {
        return JSON.parse(this.getAttribute('data-operators') || 'null') || this.getDefaultOperators() || [];
    }

    getDefaultOperators() {
        return [{
            'value': 'and',
            'label': 'et',
            'tooltip': 'toutes les valeurs sélectionnées doivent correspondre',
        }, {
            'value': 'or',
            'label': 'ou',
            'tooltip': 'au moins une valeur sélectionnée doit correspondre',
        }, {
            'value': 'nor',
            'label': 'sauf',
            'tooltip': 'aucune des valeurs sélectionnées ne doit correspondre',
        }];
    }

    getUrl() {
        return this.getAttribute('data-url') || this.getDefaultUrl();
    }

    getDefaultUrl() {
        return null;
    }

    clearInputAndProposals() {
        this.inputField.value = '';
        this.proposalsList.innerHTML = '';
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
            this.addSelectedItem({
                'value': event.target.getAttribute('data-value'),
                'label': event.target.getAttribute('data-label'),
                'url': event.target.getAttribute('data-url'),
                'tooltip': event.target.getAttribute('data-tooltip')
            });
            this.clearInputAndProposals();
            this.inputField.focus();
        }
    }

    addSelectedItem(item) {
        if (! item.label) {
            item.label = item.value;
        }

        const span = document.createElement('span');
        span.setAttribute('class', 'item');
        span.setAttribute('title', item.tooltip || '');
        span.innerHTML = item.url ? '<a href="' + item.url + '">' + item.label + '</a>' : item.label;
        this.insertBefore(span, this.inputField);

        const input = document.createElement('input');
        input.setAttribute('type', 'hidden');
        input.setAttribute('name', this.getAttribute('name'));
        input.setAttribute('value', item.value);
        span.appendChild(input);

        const button = document.createElement('button');
        button.innerHTML = '&times;';
        button.setAttribute('type', 'button');
        button.setAttribute('class', 'remove');
        button.setAttribute('title', 'supprimer cet élément');
        button.addEventListener('click', function(event) {
            span.parentNode.removeChild(span);
        });
        span.appendChild(button);
    }
}

////////////////////////////////////////////////////////////////////////////////

class FrancoraliteAuthoritiesAutocomplete extends FrancoraliteAutocomplete {
    parseProposal(item) {
        return {
            'value': item.id,
            'label': item.first_name + ' ' + item.last_name,
            'url': '/authority/' + item.id,
            'tooltip': null
        };
    }
}

class FrancoraliteEnumAutocomplete extends FrancoraliteAutocomplete {
    parseProposal(item) {
        return {
            'value': item.id,
            'label': item.name,
            'url': null,
            'tooltip': null
        };
    }
}

class FrancoraliteNumberEnumAutocomplete extends FrancoraliteAutocomplete {
    parseProposal(item) {
        return {
            'value': item.id,
            'label': item.number + ' : ' + item.name,
            'url': null,
            'tooltip': null
        };
    }
}

class FrancoraliteFullTextAutocomplete extends FrancoraliteAutocomplete {
    parseProposal(item) {
        return {
            'value': item,
            'label': item,
            'url': null,
            'tooltip': null,
        };
    }
}

////////////////////////////////////////////////////////////////////////////////

class FrancoraliteCivility extends FrancoraliteFullTextAutocomplete {
    getDefaultUrl() {
        return '/api/civility/?limit=50&search=';
    }
}

class FrancoraliteCodeExternal extends FrancoraliteFullTextAutocomplete {
    getDefaultUrl() {
        return '/api/code_external/?limit=10&search=';
    }
}

class FrancoraliteCodeInternal extends FrancoraliteFullTextAutocomplete {
    getDefaultUrl() {
        return '/api/code_internal/?limit=10&search=';
    }
}

class FrancoraliteCoirault extends FrancoraliteNumberEnumAutocomplete {
    getDefaultUrl() {
        return '/api/skos_concept?limit=10&search=';
    }
}

class FrancoraliteCollector extends FrancoraliteAuthoritiesAutocomplete {
    getDefaultUrl() {
        return '/api/authority?limit=10&is_collector=true&ordering=first_name+last_name&search=';
    }
}

class FrancoraliteCoupe extends FrancoraliteEnumAutocomplete {
    getDefaultUrl() {
        return '/api/coupe?limit=50&search=';
    }
}

class FrancoraliteCulturalArea extends FrancoraliteFullTextAutocomplete {
    getDefaultUrl() {
        return '/api/cultural_area/?limit=50&search=';
    }
}

class FrancoraliteDance extends FrancoraliteEnumAutocomplete {
    getDefaultUrl() {
        return '/api/dance?limit=50&search=';
    }
}

class FrancoraliteDomainMusic extends FrancoraliteEnumAutocomplete {
    getDefaultUrl() {
        return '/api/domain_music?limit=50&search=';
    }
}

class FrancoraliteDomainSong extends FrancoraliteEnumAutocomplete {
    getDefaultUrl() {
        return '/api/domain_song?limit=50&search=';
    }
}

class FrancoraliteDomainTale extends FrancoraliteEnumAutocomplete {
    getDefaultUrl() {
        return '/api/domain_tale?limit=50&search=';
    }
}

class FrancoraliteDomainVocal extends FrancoraliteEnumAutocomplete {
    getDefaultUrl() {
        return '/api/domain_vocal?limit=50&search=';
    }
}

class FrancoraliteInformer extends FrancoraliteAuthoritiesAutocomplete {
    getDefaultUrl() {
        return '/api/authority?limit=10&is_informer=true&ordering=first_name+last_name&search=';
    }
}

class FrancoraliteInstrument extends FrancoraliteEnumAutocomplete {
    getDefaultUrl() {
        return '/api/instrument?limit=50&search=';
    }
}

class FrancoraliteKeyword extends FrancoraliteEnumAutocomplete {
    getDefaultUrl() {
        return '/api/keyword?limit=50&search=';
    }
}

class FrancoraliteLaforte extends FrancoraliteNumberEnumAutocomplete {
    getDefaultUrl() {
        return '/api/ref_laforte?limit=10&search=';
    }
}

class FrancoraliteLanguage extends FrancoraliteEnumAutocomplete {
    getDefaultUrl() {
        return '/api/language?limit=50&search=';
    }
}

class FrancoraliteLocation extends FrancoraliteAutocomplete {
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

class FrancoraliteMediaType extends FrancoraliteEnumAutocomplete {
    getDefaultUrl() {
        return '/api/mediatype?limit=50&search=';
    }
}

class FrancoraliteRecordingContext extends FrancoraliteEnumAutocomplete {
    getDefaultUrl() {
        return '/api/recordingcontext?limit=50&search=';
    }
}

class FrancoraliteThematic extends FrancoraliteEnumAutocomplete {
    getDefaultUrl() {
        return '/api/thematic?limit=50&search=';
    }
}

class FrancoraliteTimbre extends FrancoraliteFullTextAutocomplete {
    getDefaultUrl() {
        return '/api/timbre/?limit=50&search=';
    }
}

class FrancoraliteTimbreRef extends FrancoraliteFullTextAutocomplete {
    getDefaultUrl() {
        return '/api/timbre_ref/?limit=50&search=';
    }
}

class FrancoraliteUsefulness extends FrancoraliteEnumAutocomplete {
    getDefaultUrl() {
        return '/api/usefulness?limit=50&search=';
    }
}

customElements.define('francoralite-civility', FrancoraliteCivility);
customElements.define('francoralite-code-external', FrancoraliteCodeExternal);
customElements.define('francoralite-code-internal', FrancoraliteCodeInternal);
customElements.define('francoralite-coirault', FrancoraliteCoirault);
customElements.define('francoralite-collector', FrancoraliteCollector);
customElements.define('francoralite-coupe', FrancoraliteCoupe);
customElements.define('francoralite-cultural-area', FrancoraliteCulturalArea);
customElements.define('francoralite-dance', FrancoraliteDance);
customElements.define('francoralite-domain-music', FrancoraliteDomainMusic);
customElements.define('francoralite-domain-song', FrancoraliteDomainSong);
customElements.define('francoralite-domain-tale', FrancoraliteDomainTale);
customElements.define('francoralite-domain-vocal', FrancoraliteDomainVocal);
customElements.define('francoralite-informer', FrancoraliteInformer);
customElements.define('francoralite-instrument', FrancoraliteInstrument);
customElements.define('francoralite-keyword', FrancoraliteKeyword);
customElements.define('francoralite-laforte', FrancoraliteLaforte);
customElements.define('francoralite-language', FrancoraliteLanguage);
customElements.define('francoralite-location', FrancoraliteLocation);
customElements.define('francoralite-media-type', FrancoraliteMediaType);
customElements.define('francoralite-recording-context', FrancoraliteRecordingContext);
customElements.define('francoralite-thematic', FrancoraliteThematic);
customElements.define('francoralite-timbre', FrancoraliteTimbre);
customElements.define('francoralite-timbre-ref', FrancoraliteTimbreRef);
customElements.define('francoralite-usefulness', FrancoraliteUsefulness);
