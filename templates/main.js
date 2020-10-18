/* <script src="//unpkg.com/leaflet/dist/leaflet.js"></script> */
function openNav() {
    document.getElementById("sidenav").style.left = "0px";
    document.getElementById("sidenavclose").style.left = "280px";
    // document.getElementById("years").style.left = "280px";
  }
  
  /* Set the width of the side navigation to 0 */
  function closeNav() {
    document.getElementById("sidenav").style.left = "-270px";
    document.getElementById("sidenavclose").style.left = "-40px";
    // document.getElementById("years").style.left = "20px";
}


/* filter the nav bar*/
$(document).ready(function () {
    $("#filter").keyup(function () {
        var filter = $(this).val(),
            count = 0;
        $("ul li").each(function () {
            if (filter == "") {
                $(this).css("visibility", "visible");
                $(this).fadeIn();
            } else if ($(this).text().search(new RegExp(filter, "i")) < 0) {
                $(this).css("visibility", "hidden");
                $(this).fadeOut();
            } else {
                $(this).css("visibility", "visible");
                $(this).fadeIn();
            }
        });
    });

/* expand and collapse the nav bar */
    $( "li.expander" ).click(function() {
      $( this ).next().toggleClass( "condense" );
      $( this ).find("span").toggleClass( "ui-icon-plus" );
      $( this ).find("span").toggleClass( "ui-icon-minus" );
    });
});

