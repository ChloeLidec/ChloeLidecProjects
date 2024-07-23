
function plie_deplie_filtres() {
    const dep = document.getElementById("fleci");
    if (document.getElementById("grps_filtres").style.display == "none") {
        document.getElementById("grps_filtres").setAttribute('style', 'display:flex !important');
    } else {
        document.getElementById("grps_filtres").setAttribute('style', 'display:none !important');
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

function plie_deplie_semaines() {
    const flec = document.getElementById("flecg");
    if (document.getElementById("groupe_filtre").style.display == "none") {
        document.getElementById("groupe_filtre").style.display = "block";
    } else {
        document.getElementById("groupe_filtre").style.display = "none";
    }
    var st = window.getComputedStyle(flec, null);
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
        flec.style.transform = "rotate(-180deg)";
    }
    else {
        flec.style.transform = "rotate(0deg)";
    }
};
