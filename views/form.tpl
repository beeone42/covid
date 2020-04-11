<form id='covid-form'>
Profil Name: <input type='text' id='profil_name' name='profil_name' value='default' /><br />

Prenom:      <input type='text' name='prenom' value=''  /><br />
Nom:         <input type='text' name='nom'    value=''  /><br />

Adresse:     <input type='text' name='addr'   value=''  /><br />
Code Postal: <input type='text' name='cp'     value=''  /><br />
Ville:       <input type='text' name='ville'  value=''  /><br />
Ne le:       <input type='text' name='ne_le'  value=''  /><br />
A:           <input type='text' name='ne_a'   value=''  /><br />

<hr />

Sortie le:   <input type='text' name='sort_le' value='' /><br />
        A:   <input type='text' name='sort_hm' value='' />
              <input type='hidden' name='sort_h' value='' />
             <input type='hidden' name='sort_m' value='' /><br />
   Fait A:   <input type='text' name='fait_hm' value='' />
              <input type='hidden' name='fait_h' value='' />
             <input type='hidden' name='fait_m' value='' /><br />

<hr />

Raison:
<select name='raisons'>
  <option value='travail'>travail</option>
  <option value='courses'>courses</option>
  <option value='sante'>sante</option>
  <option value='famille'>familliale</option>
  <option value='sport'>sport / ballade</option>
  <option value='judiciaire'>judiciaire</option>
  <option value='missions'>missions</option>
</select>
<br />

<input type='submit' id='save' value='save profil'>
<input type='submit' id='delete' value='delete profil'>
<br />

<hr />

Profils:

<select size='5' id='profils'>
</select>

<br/>
<input type='submit' id='gen' value='generate'>
</form>