////////////////////
//// JavaScripts for Post Page
///

$(function() {
    $('.js-menu-icon').click(function() {
      
        // $(this) : Self element, namely div.js-menu-icon
        // next() Pop up menu
        // toggle() : Switch show and hide  
        $(this).next().toggle();
    })
})


