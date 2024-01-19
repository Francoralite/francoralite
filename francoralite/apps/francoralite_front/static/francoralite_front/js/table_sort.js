"use strict";
/* jslint node: true */
/* jshint esversion: 6 */


function configureTableHeaderSort(table, header, column_index, context) {
    var is_number = header.className.indexOf('number') >= 0;
    function getColumnValue(row, default_value) {
        var cells = row.getElementsByTagName('td');
        var offset = 0;
        for (var i = 0 ; i < cells.length ; i++) {
            var colspan = 0;
            try {
                if (cells[i].getAttribute('colspan') !== null) {
                    colspan = parseInt(cells[i].getAttribute('colspan')) - 1;
                }
            }
            catch (e) {}
            if (i + offset <= column_index && column_index <= i + offset + colspan) {
                var content = cells[i].getAttribute('data-sort-value');
                if (content === null) {
                    content = cells[i].innerHTML.replace(/<img[^>]* alt="([^"]*)"[^>]*>/g, function(match, p1) { return p1; }).replace(/<[^>]*>/g, '').replace(/\n/g, ' ');
                }
                return content === null || content.trim() === '' ? default_value : (is_number ? parseFloat(content.replace(/,/g, '.').replace(/[^0-9.-]/g, '')) : content.trim().toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, ''));
            }
            offset += colspan;
        }
        return null;
    }
    header.addEventListener('click', function() {
        var ascending = true;
        if (header === context[0] && header.className.indexOf('asc') >= 0) {
            ascending = false;
        }
        if (context[0] !== null) {
            context[0].className = context[0].className.replace(/ asc| desc/, '');
        }
        header.className = header.className + (ascending ? ' asc' : ' desc');
        context[0] = header;
        var tbody = table.getElementsByTagName('tbody')[0];
        var rows = [].slice.call(tbody.getElementsByTagName('tr'));
        if (rows.length > 0) {
            for (var i = 0 ; i < rows.length ; i++) {
                tbody.removeChild(rows[i]);
            }
            var default_value = ascending ? (is_number ? Number.POSITIVE_INFINITY : 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz') : (is_number ? Number.NEGATIVE_INFINITY : '');
            rows.sort(function (row1, row2) {
                var value1 = getColumnValue(row1, default_value);
                var value2 = getColumnValue(row2, default_value);
                return (value1 === value2) ? 0 : (value1 > value2 ? 1 : -1) * (ascending ? 1 : -1);
            });
            for (var i = 0 ; i < rows.length ; i++) {
                tbody.appendChild(rows[i]);
            }
        }
    });
}

var tables = document.getElementsByTagName('table');
for (var i = 0 ; i < tables.length ; i++) {
    var headers = tables[i].getElementsByTagName('th');
    var lines_count = tables[i].getElementsByTagName('tbody')[0].getElementsByTagName('tr').length;
    var table_context = [null];
    for (var j = 0 ; j < headers.length ; j++) {
        if (lines_count > 1 && headers[j].className.indexOf('sortable') >= 0) {
            configureTableHeaderSort(tables[i], headers[j], j, table_context);
            headers[j].className = headers[j].className + ' active_sort';
        }
    }
}
