$(document).ready( function() {
  var updateFontSize = function(elem) {
    var fontStep = 1;
    var parentWidth = $(elem).width();
    var parentHeight = parseInt($(elem).css('max-height'), 10);
    var childElem = $(elem).find('span');
    while ((childElem.width() > parentWidth) || (childElem.height() > parentHeight)) {
      childElem.css('font-size', parseInt(childElem.css('font-size'), 10) - fontStep + 'px');
    }
  };

  if(($('#funnel-proposals').length)) {
    $.ajax({
      type: 'GET',
      dataType: 'jsonp',
      url: window.EventDetails.proposal_url,
      success: function(data) {
        $("#funnel-proposals p.loadingtxt").hide();
        var proposalsTemplate = $('#proposals-wrapper').html();
        $("#funnel-proposals").append(Mustache.render(proposalsTemplate, data));
        $.each($('.proposal-card .title'), function(index, title) {
          updateFontSize(title);
        });
      }
    });//eof ajax call
  }
});