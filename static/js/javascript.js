 // var mass_header_img = ['/static/images/1.jpeg', '/static/images/10.jpeg', '/static/images/7.jpeg', '/static/images/4.jpeg'];
// var i = 0;

// function sliderHeader()
// {
// 	document.getElementsByClassName("slider_header")[0].style.backgroundImage = "url(" + mass_header_img[i] + ")";
	
// 	i++;

// 	if (i == mass_header_img.length) 
// 	{
// 		i=0;
// 	}
// }
// setInterval(sliderHeader, 3000);


// document.getElementById('button_review').onclick = function()
// {
//     document.getElementById('form_feedback').classList.add('block_active')
// }


// $('#button_to_contact_us').click(function() {
//     $('#block_to_contact_us').addClass('block_active');
// });


document.getElementById('button_to_contact_us').onclick = function()
{
    document.getElementById('block_to_contact_us').classList.add('block_active');
}

document.getElementById('button_close_block_to_contact_us').onclick = function()
{
    document.getElementById('block_to_contact_us').classList.remove('block_active');
}


document.getElementsByClassName('menu_toggle')[0].onclick = function()
{
    document.getElementsByClassName('bottom_right_block_header_links')[0].classList.toggle('block_active');
}

$(window).scroll(function(){
  var docscroll = $(window).scrollTop();
  if(docscroll > $('.top_block_header').height())
  {
    // $('.bottom_block_header').css({'height': $('.bottom_block_header').height(),'width': $('.bottom_block_header').width()}).addClass('fixed');
    $('.bottom_block_header').addClass('fixed');
    $('main').css({'margin-top': $('.bottom_block_header').height()});
  }

  else
  {
    $('.bottom_block_header').removeClass('fixed');
    $('main').css({'margin-top':'0px'});
  }
});






var slideIndex = 1;
showSlides(slideIndex);

/* Функция увеличивает индекс на 1, показывает следующй слайд*/
function plusSlide() {
    showSlides(slideIndex += 1);
}

/* Функция уменьшяет индекс на 1, показывает предыдущий слайд*/
function minusSlide() {
    showSlides(slideIndex -= 1);  
}

/* Устанавливает текущий слайд */
function currentSlide(n) {
    showSlides(slideIndex = n);
}

/* Основная функция слайдера */
function showSlides(n) {
    var i;
    var slides = $(".block_carousel img");
    if (n > slides.length) {
      slideIndex = 1
    }

    if (n < 1) {
        slideIndex = slides.length
    }

    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }

    for (i = 0; i < slides.length; i++) {
        slides[i].className = slides[i].className.replace("active");
    }
    slides[slideIndex - 1].style.display = "block";
}
















// $('#button_to_contact_us').click(function() {
//     $('#block_to_contact_us').addClass('block_active');
// });


// window.onscroll = function() 
// {
// 	var nav = document.querySelector[1]('nav');

// 	if (window.pageYOffset > 210)
// 	{
// 		nav.classList.add('nav_fixed');
// 	}

// 	else if(window.pageYOffset < 900)
// 	{
// 		nav.classList.remove('nav_fixed');
// 	}
// }

// window.onscroll = function()
// {
// 	var nav = document.querySelector('nav')

	

// 	if (window.pageYOffset > 658)
// 	{
// 		nav.getElementsByClassName("nav_fixed").style.display = "none";
// 	}

// 	else if(window.pageYOffset < 658)
// 	{
		
// 	}
// }