function plie_deplie_matieres() {
    const dep = document.getElementById("fleci");
    if (document.getElementById("matieres_gauche").style.display == "none") {
        document.getElementById("matieres_gauche").setAttribute('style', 'display:flex !important');
    } else {
        document.getElementById("matieres_gauche").setAttribute('style', 'display:none !important');
    }
    var st = window.getComputedStyle(dep, null);
    var tr = st.getPropertyValue("-webkit-transform") ||
        st.getPropertyValue("-moz-transform") ||
        st.getPropertyValue("-ms-transform") ||
        st.getPropertyValue("-o-transform") ||
        st.getPropertyValue("transform") ||
        "fail...";
    var angle = 0;
    if (tr !== "none") {
        var values = tr.split('(')[1];
        values = values.split(')')[0];
        values = values.split(',');
        var a = values[0];
        var b = values[1];

        angle = Math.round(Math.atan2(b, a) * (180 / Math.PI));
    }
    if (angle == 0) {
        dep.style.transform = "rotate(-180deg)";
    }
    else {
        dep.style.transform = "rotate(0deg)";
    }
};
function collapse() {
    // this.classList.toggle("active");
    var content = document.getElementById("content");
    var bt = document.getElementById("collapsible");
    if (content.style.display === "block") {
        content.style.display = "none";
        bt.innerHTML = '<img src="static/img/plus.png" alt="+" height="10em">'
    } else {
        content.style.display = "block";
        bt.innerHTML = '<img src="static/img/moins.png" alt="-" height="10em">'
    }
};
