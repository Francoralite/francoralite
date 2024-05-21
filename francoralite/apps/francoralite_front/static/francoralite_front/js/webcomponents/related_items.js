"use strict";
/* jslint node: true */
/* jshint esversion: 6 */
/* globals customElements */

// <francoralite-related-items></francoralite-related-items>
class FrancoraliteRelatedItems extends HTMLElement {
    /**
     * Initializes the constructor for the FrancoraliteRelatedItems class.
     *
     * This constructor sets the `thesaurus` and `valueFilter` attributes based on the attributes of the element.
     * It also sets the display and position styles of the element.
     * It creates two buttons using the `createButton` function and appends them to the element.
     *
     * @return {void}
     */
    constructor() {
        super(); 
        this.thesaurus = this.getAttribute('thesaurus');
        this.valueFilter = this.getAttribute('filter_value');

        this.style.display = 'inline-block';
        this.style.position = 'relative';
        this.alignment = 'center';
        this.style.left = '50%';
        this.style.transform = 'translateX(-50%)';

        const createButton = (related, caption) => {
            const button = document.createElement('button');
            button.setAttribute('class', 'btn');
            button.setAttribute('type', 'button');
            button.setAttribute('id', 'btn-' + related + '-related');
            button.innerHTML = `<span class="glyphicon glyphicon-search"></span> Rechercher les <b>${caption}</b> ...`;
            Object.assign(button.style, {
                backgroundColor: '#ef7c56',
                color: 'black',
                position: 'relative',
                margin: '10px',
                cursor: 'pointer',
            });
            this.appendChild(button);
            return button;
        };

        this.buttonItem = createButton('item', 'items');
        this.buttonCollection = createButton('collection', 'enquêtes');

    }
    connectedCallback() {
        this.buttonItem.addEventListener('click', () => this.navigateToUrl());
        this.buttonCollection.addEventListener('click', () => this.navigateToUrl('collection'));
    }
    disconnectedCallback() {
        this.buttonItem.removeEventListener('click', () => this.navigateToUrl());
        this.buttonCollection.removeEventListener('click', () => this.navigateToUrl('collection'));
    };

    navigateToUrl(request_type = 'item') {
        const baseUrl = '/search_advanced/';
        const params = new URLSearchParams({
            request_type: request_type,
        });

        window.location.href = `${baseUrl}?${params.toString()}&${this.thesaurus}=${this.valueFilter}`;
    }
}

customElements.define('francoralite-related-items', FrancoraliteRelatedItems);