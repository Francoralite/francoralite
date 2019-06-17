function selectionCallback(abcelem) {
  var note = {};
  for (var key in abcelem) {
    if (abcelem.hasOwnProperty(key) && key !== "abselem") {
      note[key] = abcelem[key];
    }
  }
}

function colorRange(range, color) {
  if (range && range.elements) {
    range.elements.forEach(function (set) {
      set.forEach(function (item) {
        //item.attr({fill: color});
        item.style.fill = color;
      });
    });
  }
}

function animateCallback(lastRange, currentRange, context) {
  colorRange(lastRange, "#000000");
  colorRange(currentRange, "#92b220");
}

function initEditor() {
  var abc_editor = new ABCJS.Editor("id_melody", {
    paper_id: "paper0",
    generate_midi: true,
    midi_id: "midi",
    midi_download_id: "midi-download",
    generate_warnings: true,
    warnings_id: "warnings",
    setRandomProgress: 0.33,
    abcjsParams: {
      responsive: "resize",
      generateDownload: true,
      clickListener: selectionCallback,
      inlineControls: {
        loopToggle: true,
        //tempo: true,
      },
      animate: {
        listener: animateCallback,
        qpm: 120,
      },
    },
  });
}

window.addEventListener("load", initEditor, false);
