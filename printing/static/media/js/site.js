// JavaScript Document
	$(function() {
		//	Responsive layout, resizing the items
		$('#pl_spl_offers ul').carouFredSel({
			auto: false,
			prev: '#prev_pdt',
			next: '#next_pdt',
			scroll: 1,
			items: 4,
			circular: false,
			infinite: false
		});
		
		//	Fuild layout, centering the items
		$('#pl_client_logos ul').carouFredSel({
			auto : {
					items           : 5,
					duration        : 7500,
					easing          : "linear",
					timeoutDuration : 0,
					pauseOnHover    : "immediate"
				}
		});
		
		/************************************
		DROPDOWN MENU CONTENT
		************************************/
			
		$(".tab_content").hide();
		$(".tab_content:first").show();  
		
		$(".cat_list li a").hover(function() {
			$(".cat_list li a").removeClass("active");
			$(this).addClass("active");
			$(".tab_content").hide();
			var activeTab = $(this).attr("rel"); 
			$("#"+activeTab).show(); 
		});	
		
		
				
		$("#pl_left_navigation").accordion({ 
			header: "li.header > a",
			autoHeight: false,
			active: false			
			});
			
		
		$("#pl_left_navigation ul li a").click(function(){
				
				$('#pl_left_navigation_listing ul li ').removeClass('current-menu-ancestor')
			
			});

		
		
		$('.royalSlider').royalSlider({
			arrowsNav: false,
			fadeinLoadedSlide: true,
			controlNavigationSpacing: 0,
			controlNavigation: 'thumbnails',
			
			deeplinking: {
    		// deep linking options go gere
    		change: true,
    		prefix: 'slider-'
			},

			thumbs: {
			  autoCenter: false,
			  fitInViewport: true,
			  orientation: 'vertical',
			  spacing: 0,
			  paddingBottom: 0
			},
			keyboardNavEnabled: true,
			imageScaleMode: 'fill',
			imageAlignCenter:true,
			slidesSpacing: 0,
			loop: false,
			loopRewind: true,
			numImagesToPreload: 3,
			sliderDrag: false,
			video: {
			  autoHideArrows:true,
			  autoHideControlNav:false,
			  autoHideBlocks: true
			}, 
			autoScaleSlider: true, 
			autoScaleSliderWidth: 708,     
			autoScaleSliderHeight: 289,

			/* size of all images http://help.dimsemenov.com/kb/royalslider-jquery-plugin-faq/adding-width-and-height-properties-to-images */
			imgWidth: 713,
			imgHeight: 289

		  });
		  
		

	});