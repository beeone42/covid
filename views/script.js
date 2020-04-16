
g_profils = {}

function show_profil_data(profil_id)
{
    if (!(profil_id in g_profils))
	return ;
    profil = g_profils[profil_id]
    var datas = array_to_obj($("#covid-form").serializeArray());
    for (const i in profil)
    {
	if (i in datas)
	{
	    if ((i != 'sort_le') && (i != 'sort_hm') && (i != 'fait_hm'))
		$("input[name=" + i + "]").val(profil[i]);
	}
    }
}

function get_profil_data(profil_id)
{
    profil_str = localStorage.getItem("profil_" + profil_id)
    console.log(profil_str)
    if (profil_str != null && profil_str != '')
    {
	profil = JSON.parse(profil_str);
	g_profils[profil_id] = profil;
	console.log('profile ' + profil_id + ' loaded');
    }
    else
    {
	console.log('profile ' + profil_id + ' not found');
    }
}

function update_profils_list()
{
    $s = $("select#profils");
    $s.html("");
    for (const p in g_profils)
    {
	console.log("--> " + p);
	$s.append($("<option />").val(p).text(p));
    }
    $s.change(function() {
	show_profil_data($("select#profils").val());
    });
}

function get_profils()
{
    profils_str = localStorage.getItem("profils")
    console.log(profils_str)
    if (profils_str != null && profils_str != '')
    {
	profils = JSON.parse(profils_str);
	console.log(profils)
	profils.forEach(p => get_profil_data(p));
	update_profils_list()
    }
    else
    {
	console.log('no profile yet')
    }
}

function save_profil(profil, datas)
{
    g_profils[profil] = datas;
    localStorage.setItem("profil_" + profil, JSON.stringify(datas));
    localStorage.setItem("profils", JSON.stringify(Object.keys(g_profils)));
    update_profils_list()
}

function delete_profil(profil)
{
    delete g_profils[profil];
    localStorage.removeItem("profil_" + profil);
    localStorage.setItem("profils", JSON.stringify(Object.keys(g_profils)));
    update_profils_list()
}

function array_to_obj(datas)
{
    res = {};
    datas.forEach(e => res[e.name] = e.value);
    return (res)
}

$(function(){

    console.log("start covid generator, stay home, stay safe");
    get_profils();
    
    var now = new Date();
    $("input[name=sort_le]").val(now.toLocaleDateString('fr-FR'));
    $("input[name=sort_hm]").val(now.toLocaleTimeString('fr-FR').substring(0,5));
    
    now.setMinutes(now.getMinutes() - 7);
    $("input[name=fait_hm]").val(now.toLocaleTimeString('fr-FR').substring(0,5));


    $('button#save').click(function() {
	console.log('click save');
	var datas = array_to_obj($("#covid-form").serializeArray());
	profil_id = $("#profil_name").val();
	save_profil(profil_id, datas);
    });
    
    $('button#delete').click(function() {
	console.log('click delete');
	profil_id = $("#profil_name").val();
	delete_profil(profil_id, datas);
    });
    
    $('button#gen').click(function() {
	
	console.log('click gen');
	
	$("input[name=sort_h]").val($("input[name=sort_hm]").val().split(':')[0])
	$("input[name=sort_m]").val($("input[name=sort_hm]").val().split(':')[1])
	
	$("input[name=fait_h]").val($("input[name=fait_hm]").val().split(':')[0])
	$("input[name=fait_m]").val($("input[name=fait_hm]").val().split(':')[1])

	var form_data = $("#covid-form").serialize();
	
	$.post('gen', form_data, function( data ) {
	    console.log(data);
	    window.location.href = "pdf/" + data;
	});
    });

    $('button#url').click(function() {
	console.log('click url');
	var form_data = $("#covid-form").serialize();
	ref = window.location.protocol + '//'+ window.location.hostname + window.location.pathname + 'gen?' +  form_data + '&auto=1';
	console.log(ref);
	$("span#url").html('<a href="'+ref+'">'+$("#profil_name").val() + '-' + $("select[name=raisons]").val() + '</a>')
    });

   
    $('form').submit(function(event){
	event.preventDefault();
	return false;
    });

   
});

