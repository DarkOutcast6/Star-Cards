// NOTE: DON'T USE THIS FOR ACTUAL SERVERS WITH BACKEND!
// HAVE ACTUAL PATHS!

if(/Android|webOS|iPhone|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)){
	location.replace("mobile.html");
  document.write("mobile");
}

function hideAlert() {
	document.elm.style.visibility = "hidden";
}

