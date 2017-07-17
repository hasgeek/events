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

  var getElemWidth = function(elem) {
    var card_width = $(elem).css('width');
    var card_margin = $(elem).css('margin-left');
    var card_total_width = parseInt(card_width, 10) + 2.5 * parseInt(card_margin, 10);
    return card_total_width;
  };

  var enableScroll = function(items_length) {
    $(".mCustomScrollbar").css('width', items_length * getElemWidth(".proposal-card") + 'px');
    $('.mCustomScrollbar').mCustomScrollbar({ axis:"x", theme: "dark-3", scrollInertia: 10, alwaysShowScrollbar: 0});
  };

  function parseProposalJson(json) {
    var proposal_ractive = new Ractive({
      el: '#funnel-proposals',
      template: '#proposals-wrapper',
      data: {
        proposals: json.proposals
      },
      complete: function() {
        $.each($('.proposal-card .title'), function(index, title) {
          updateFontSize(title);
        });

        //Set width of content div to enable horizontal scrolling
        enableScroll(json.proposals.length);

        $(window).resize(function() {
          enableScroll(json.proposals.length);
        });
      }
    });
  };

  if(($('#funnel-proposals').length)) {
    $.ajax({
      type: 'GET',
      dataType: 'jsonp',
      url: window.Event.proposal_url,
      success: function(data) {
        parseProposalJson(data);
      }
    });//eof ajax call
  }
});