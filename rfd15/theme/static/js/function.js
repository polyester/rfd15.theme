jQuery(document).ready(function() {

jQuery(document).ready(function(jq) {

var buscalink = document.location.href + '/search';

jQuery("#searchbt a").attr({
          href:buscalink
        });

});

jQuery('#searchbt a').prepOverlay({
                subtype: 'ajax',
                filter: '#content>*',
                });
});
jQuery( function($) {
  $('img.image-right, img.image-left, img.image-inline, img.eventImage, img.newsImage')
    .prepOverlay({
      subtype: 'image',
      urlmatch: '/image_.+$',
      urlreplace: '/image_large'
      });
});
