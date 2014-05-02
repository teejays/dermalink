<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<head lang="en">
	<meta http-equiv="content-type" content="text/html;charset=utf-8">
	<title>Template Documentation Template</title>
	<!-- Framework CSS -->
	<link rel="stylesheet" href="assets/blueprint-css/screen.css" type="text/css" media="screen, projection">
	<link rel="stylesheet" href="assets/blueprint-css/print.css" type="text/css" media="print">
	<!--[if lt IE 8]><link rel="stylesheet" href="assets/blueprint-css/ie.css" type="text/css" media="screen, projection"><![endif]-->
	<link rel="stylesheet" href="assets/blueprint-css/plugins/fancy-type/screen.css" type="text/css" media="screen, projection">
	<style type="text/css" media="screen">
		p, table, hr, .box { margin-bottom:25px; }
		.box p { margin-bottom:10px; }
	</style>
</head>


<body>
	<div class="container">
	
		<h3 class="center alt">&ldquo;Rocket&rdquo; Documentation by &ldquo;Ulziibat Nansaltsog&rdquo; v1.0</h3>
		
		<hr>
		
		<h1 class="center">&ldquo;Rocket Landing Page&rdquo;</h1>
		
		<div class="borderTop">
			<div class="span-6 colborder info prepend-1">
				<p class="prepend-top">
					<strong>
					Created: 17/11/2013<br>
					By: Ulziibat Nansaltsog<br>
					Email: <a href="mailto:olziinaa@gmail.com">olziinaa@gmail.com</a>
					</strong>
				</p>
			</div><!-- end div .span-6 -->		
	
			<div class="span-12 last">
				<p class="prepend-top append-0">Thank you for purchasing my theme. If you have any questions that are beyond the scope of this help file, please feel free to email via my user page contact form <a href="http://themeforest.net/user/olziinaa">here</a>. Thanks so much!</p>
			</div>
		</div><!-- end div .borderTop -->
		
		<hr>
		
		<h2 id="toc" class="alt">Table of Contents</h2>
		<ol class="alpha">
			<li><a href="#included">What's included</a></li>
			<li><a href="#htmlStructure">HTML Structure</a></li>
			<li><a href="#cssFiles">CSS Files and Structure</a></li>
			<li><a href="#javascript">JavaScript</a></li>
			<li><a href="#credits">Sources and Credits</a></li>
			<li><a href="#">Any additional unique features that need an overview</a></li>
		</ol>
		
		<hr>
		<h3 id="included"><strong>What's included</strong> - <a href="#toc">top</a></h3>
		<p>Within the download you'll find the following directories and files, logically grouping common resources and providing both compiled and minified variations.</p>
		<p>Once downloaded, unzip the compressed folder to see the structure of (the compiled) Rocket. You'll see something like this</p>
		<pre><code class="bash">
		index.html
		demo/
		assets/
		│   ├── demo-images
		├── css/
		│   ├── animate.css
		│   ├── bootstrap.min.css
		│   ├── prettyPhoto.css
		│   └── style.css
		├── js/
		│   ├── bootstrap.js
		│   └── ie8-responsive-file-warning.js
		│   └── jquery-1.10.2.min.js
		│   └── jquery.localscroll.min.js
		│   └── jquery.prettyPhoto.js
		│   └── jquery.scrollto.min.js
		│   └── waypoints.min.js
		│   └── scripts.js
		└── fonts/
		    ├── glyphicons-halflings-regular.eot
		    ├── glyphicons-halflings-regular.svg
		    ├── glyphicons-halflings-regular.ttf
		    └── glyphicons-halflings-regular.woff
		</code></pre>
		
		<h3 id="htmlStructure"><strong>HTML Structure</strong> - <a href="#toc">top</a></h3>
		<p>This landing pages is a Based on Bootstrap 3.0. You will help bootstrap documentation on customize html & grids & layouts.</p>
		<img src="assets/images/htmlstructure.png" alt="HTML Structure" />
		<p>You can create full width div with background color & color. After use bootstrap structure. It will very simple & easy to use.</p>
		<img src="assets/images/htmlstructure2.png" alt="HTML Structure" />
		<p>If you would like to edit the color, font, or style of any elements in one of these columns, you would do the following:</p>

<pre>	#you-section {
		background-color: #someColor
		color: #someColor;
	} 
</pre>

		<p>If you don't like section padding.</p>

		<p>I.E.</p>

<pre>	.section {
		padding-top: 0px;
		padding-bottom: 0px;
	}
</pre>

		<p>So, to ensure that your new styles are applied, make sure that they carry enough "weight" and that there isn't a style lower in the CSS file that is being applied after yours.</p> 

		<hr>

		<h3 id="cssFiles"><strong>B) CSS Files and Structure</strong> - <a href="#toc">top</a></h3>

		<p>I'm using 4 CSS files in this theme. The first one is bootstrap.min.css file. Many browser interpret the default behavior of html elements differently. By using a Bootstrap CSS file, we can work round this. This file also contains some general styling, such as anchor tag colors, font-sizes, etc. Keep in mind, that these values might be overridden somewhere else in the file.</p> 

		<p>The style.css contains all of the specific stylings for the page. The file is separated into sections using:</p>  

<pre>	
/*	Section
	==================================================*/
.section {
	padding: 100px 0; // Section Padding
}

/*	Parallax Background
	==================================================*/

#parallax {
  height: 680px;
  width: 100%;
  position: fixed;
  background: url('../../demo/man1.jpg') center center no-repeat; // Please replace your image
  background-size: cover;
  z-index: -100;
}

/*	Hero
	==================================================*/
#hero {
	background: rgba(0, 0, 0, 0);
	margin-top: 80px;
	padding: 150px 0;
	color: #000;
}
#hero h1 {
	font-size: 60px; // Top slider big font size
	
}
#hero p.lead {
	font-size: 1.8em; // Top Slider Text font size
}

/*	Features
	==================================================*/ 
#features {
	background-color: #FFF;
}
.overview, .service-block {
	text-align: center;
}
.overview .lead {
	margin-bottom: 40px;
}

.service-block .glyphicon {
	font-size: 60px;
	margin-bottom: 20px;
}

</pre>
<p>prettyPhoto.css - for Gallery Lightbox</p>
<p>animate.css is a bunch of cool, fun, and cross-browser animations for you to use in your projects. Great for emphasis, home pages, sliders, and general just-add-water-awesomeness.</p>
<pre>
< yourtag class="animate" data-animate="fadeInDown" >.....< /yourtag >
</pre>
<p>You can change the duration of your animations, add a delay or change the number of times that it plays!<p>
<pre>
#yourElement {
    -vendor-animation-duration: 3s;
    -vendor-animation-delay: 2s;
    -vendor-animation-iteration-count: infinite;
}
</pre>
<strong>Animation Names</strong>
<p>Attention seekers:<br />
flash bounce shake tada swing wobble pulse</p>

<p>Flippers (currently Webkit, Firefox, & IE10 only):<br />

flip flipInX flipOutX flipInY flipOutY</p>

<p>Fading entrances:<br />

fadeIn fadeInUp fadeInDown fadeInLeft fadeInRight fadeInUpBig fadeInDownBig fadeInLeftBig fadeInRightBig</p>

<p>Fading exits:<br />

fadeOut fadeOutUp fadeOutDown fadeOutLeft fadeOutRight fadeOutUpBig fadeOutDownBig fadeOutLeftBig fadeOutRightBig</p>

<p>Bouncing entrances:<br />

bounceIn bounceInDown bounceInUp bounceInLeft bounceInRight</p>

<p>Bouncing exits:<br />

bounceOut bounceOutDown bounceOutUp bounceOutLeft bounceOutRight</p>

<p>Rotating entrances:<br />

rotateIn rotateInDownLeft rotateInDownRight rotateInUpLeft rotateInUpRight</p>

<p>Rotating exits:<br />

rotateOut rotateOutDownLeft rotateOutDownRight rotateOutUpLeft rotateOutUpRight</p>
		<hr>
		
		<h3 id="javascript"><strong>C) JavaScript</strong> - <a href="#toc">top</a></h3>
		
		<p>This theme imports three Javascript files.</p>
		
		<ol>
			<li>bootstrap.js</li>
			<li>ie8-responsive-file-warning.js - Intended to prevent false-positive bug reports about responsive styling supposedly not working in IE8.</li>
			<li>jquery-1.10.2.min.js</li>
			<li>jquery.localscroll.min.js - Animated scrolling navigation, using anchors.</li>
			<li>jquery.prettyphoto.js - Lightbox clone for jQuery</li>
			<li>jquery.scrollto.min.js - make a small, customizable plugin for scrolling elements, or the window itself.</li>
			<li>waypoints.min.js - Waypoints is a jQuery plugin that makes it easy to execute a function whenever you scroll to an element.</li>
			<li>scripts.js - for rocket</li>
		</ol>
		  
		<strong>Scripts.js</strong>
		<pre>
function parallax() {
	var scrollPosition = $(window).scrollTop();
	$('#parallax').css('top',(80 - (scrollPosition * 0.3))+'px' ); // bg image moves at 30% of scrolling speed
	$('#hero').css('opacity',((100 - scrollPosition/2) *0.01));
}
$(document).ready(function() {

	/*	Parallax Background
	================================================== */

	$(window).on('scroll', function(e) {
		parallax();
	});
	
	/*	Local Scroll
	================================================== */
	
	jQuery('.navbar').localScroll({
			offset: -80,
			duration: 500
		});
		
	/*	Active Menu
	================================================== */
		
	jQuery(function() {
		var sections = jQuery('section');
		var navigation_links = jQuery('nav a');
		sections.waypoint({
		handler: function(direction) {
			var active_section;
			active_section = jQuery(this);
			if (direction === "up") active_section = active_section.prev();
			var active_link = jQuery('nav a[href="#' + active_section.attr("id") + '"]');
			navigation_links.parent().removeClass("active");
			active_link.parent().addClass("active");
			active_section.addClass("active-section");
		},
		offset: '35%'
		});
	});
	
	/*	Animation with Waypoints
	================================================== */
	
	jQuery('.animate').waypoint(function() {
	     var animation = jQuery(this).attr("data-animate");
	     jQuery(this).addClass(animation);
	     jQuery(this).addClass('animated');
	}, { offset: '80%' });
	
	/*	Pretty Photo
	================================================== */
	
	jQuery('#gallery a').attr('rel', 'prettyPhoto');
	jQuery("a[rel^='prettyPhoto']").prettyPhoto();
	
	/*	Bootstrap Carousel
	================================================== */
	
	jQuery('.carousel').carousel()
	

});
		</pre>
		
		<hr>
		
		<h3 id="credits"><strong>E) Sources and Credits</strong> - <a href="#toc">top</a></h3>
		
		<p>I've used the following images, icons or other files as listed.
		
		<ul>
			<li>Gallery Demo Images - <a href="http://dribbble.com/RZDESIGN" title="Ricardo de Zoete">Ricardo de Zoete</a></li>
			<li>Slider Demo Images- <a href="http://www.behance.net/Zschunke" alt="">Christian Zschunke</a></li>
			<li>Parallax Image - <a href="http://photodune.net/user/baranq" title="baranq">Baranq</a></li>
			<li><a href="http://www.getbootstrap.com" title="">Bootstrap</a> v3.0.2 by <a href="https://twitter.com/mdo" title="">@mdo</a> and <a href="https://twitter.com/fat" title="fat">@fat</a></li>
			<li>Flat Screen & Device Shapes (.CSH) by <a href="http://dribbble.com/oliverlong" title="">Oliver Long</a></li>
			<li>jQuery by <a href="http://www.jquery.com">jQuery Foundation, Inc</a></li>
			<li>Pretty Photo by <a href="http://www.no-margin-for-errors.com" title="">Stephane Caron</a></li>
			<li>jQuery Local scroll & jQuery Scroll To by <a href="http://flesler.blogspot.com" title="">Ariel Flesler</a></li>
			<li>jQuery waypoints by <a href="https://github.com/imakewebthings/jquery-waypoints/" title="">Caleb Troughton</a></li>
			<li></li>
		</ul>
		
		<hr>
		
		<p>Once again, thank you so much for purchasing this theme. As I said at the beginning, I'd be glad to help you if you have any questions relating to this theme. No guarantees, but I'll do my best to assist. If you have a more general question relating to the themes on ThemeForest, you might consider visiting the forums and asking your question in the "Item Discussion" section.</p> 
		
		<p class="append-bottom alt large"><strong>Ulziibat Nansaltsog</strong></p>
		<p><a href="#toc">Go To Table of Contents</a></p>
		
		<hr class="space">
	</div><!-- end div .container -->
</body>
</html>