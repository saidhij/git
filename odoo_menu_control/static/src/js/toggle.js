// $(document).ready(function () {
    // $(".toggle_topmenu").click(function() {
            // $("oe_main_menu_navbar").slideToggle({
            // width: 'toggle'
        // }, 0);
    // });
// });




$(document).ready(function(){
    $(".toggle_topmenu").click(function(){
        $(".navbar-inverse").animate({
            height: 'toggle'
        });
    });
});



$(document).ready(function(){
    $(".toggle_submenu").click(function(){
        $(".o_sub_menu").fadeToggle();
    });
});


// $(document).ready(function(){
    // $(".hide_submenu").click(function(){
        // $(".o_sub_menu").hide();
    // });
    // $(".show_submenu").click(function(){
        // $(".o_sub_menu").show();
    // });
// });