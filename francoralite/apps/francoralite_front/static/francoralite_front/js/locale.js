var localeStrings = {
    'title': 'titre',
    'description': 'description',
    'delete the marker permanently?': 'supprimer le marqueur de manière définitive ?',
    'marker added to the selected playlist': 'marker added to the selected playlist',
    'item added to the selected playlist': 'item added to the selected playlist',
    'collection added to the selected playlist': 'collection added to the selected playlist',
    'resource added to the selected playlist': 'resource added to the selected playlist',
    'there are unsaved or modified markers': 'il y a des marqueurs modifiés ou non sauvegardés',
    'If you exit the page you will loose your changes' : 'If you exit the page you will loose your changes',
    'author' : 'auteur',
    'Paste HTML to embed player in website': 'Paste HTML to embed player in website',
    'delete the item permanently?' : 'Supprimer définitivement l\'item ?',
    'delete the collection permanently?' : 'delete the collection permanently?',
    'delete the playlist permanently?' : 'delete the playlist permanently?',
    'delete the resource from the playlist permanently?' : 'delete the resource from the playlist permanently?',
    'delete field' : 'delete field',
    'final query' : 'final query',
    '(playlisted)' : '(playlisted)',
};

function gettrans(str){
    var loc = localeStrings; //instantiate once for faster lookup
    return str in loc ? loc[str] : str;
}
