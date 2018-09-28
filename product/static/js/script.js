// JavaScript Document
jQuery(document).ready(function(){ 'use strict';
	$(".mbuy>li").mouseover(function(){
		$(this).children(".sbuy").stop().slideDown();
	});
	
	$(".mbuy>li").mouseleave(function(){
		$(this).children(".sbuy").stop().slideUp();
	});
});