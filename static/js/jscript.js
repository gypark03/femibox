// JavaScript Document
jQuery(document).ready(function(){"use strict";
 $(".nav>li").mouseover(function(){
  $(this).children(".submenu").stop().slideDown();
  });
	
 $(".nav>li").mouseleave(function(){
  $(this).children(".submenu").stop().slideUp();
 });

 $(".mbuy>li").mouseover(function(){
		$(this).children(".sbuy").stop().slideDown();
	});
	
	$(".mbuy>li").mouseleave(function(){
		$(this).children(".sbuy").stop().slideUp();
	});
});

var win;

function winOpen(){
	win = window.open('campaign_form.html','child','toolbar=no, location=no, status=no, menubar=no, resizable=no, scrollbar=no, width=500, height=300');
}