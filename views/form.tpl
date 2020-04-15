<form id='covid-form'>

  <div class="form-row">
  <div class="form-group col-md-4">
    <label for="profil_name">Profil Name:</label>
    <input type='text' class='form-control' id='profil_name' name='profil_name' value='default' />
  </div>
  <div class="form-group col-md-4">
    <label for="prenom">Prenom:</label>
    <input type='text' class='form-control'  name='prenom' value=''  /><br />
  </div>
  <div class="form-group col-md-4">
    <label for="nom">Nom:</label>
    <input type='text' class='form-control' name='nom'    value=''  /><br />
  </div>
  </div>

  <div class="form-row">
  <div class="form-group col-md-4">
    <label for="addr">Adresse:</label>
    <input type='text' class='form-control' name='addr'   value=''  /><br />
  </div>
  <div class="form-group col-md-4">
    <label for="cp">Code Postal:</label>
    <input type='text' class='form-control' name='cp'     value=''  /><br />
  </div>
  <div class="form-group col-md-4">
    <label for="ville">Ville:</label>
    <input type='text' class='form-control' name='ville'  value=''  /><br />
  </div>
  </div>
  
  <div class="form-row">
  <div class="form-group col-md-4">
    <label for="ne_l">Né le:</label>
    <input type='text' class='form-control' name='ne_le'  value=''  /><br />
  </div>
  <div class="form-group col-md-8">
    <label for="ne_a">A:</label>
    <input type='text' class='form-control' name='ne_a'   value=''  /><br />
  </div>
  </div>

  <div class="form-row">
  <div class="form-group col-md-4">
    <label for="sort_le">Sortie le:</label>
    <input type='text' class='form-control' name='sort_le' value='' /><br />
  </div>
  <div class="form-group col-md-4">
    <label for="sort_hm">A:</label>
    <input type='text' class='form-control' name='sort_hm' value='' />
    <input type='hidden' name='sort_h' value='' />
    <input type='hidden' name='sort_m' value='' /><br />
  </div>
  <div class="form-group col-md-4">
    <label for="fait_hm">Fait A:</label>
    <input type='text' class='form-control' name='fait_hm' value='' />
    <input type='hidden' name='fait_h' value='' />
    <input type='hidden' name='fait_m' value='' /><br />
  </div>
  </div>


  <div class="form-row">
  <div class="form-group col-md-6">
    <label for="raisons">Raison:</label>
    <select size='5' id='raisons' name='raisons' class='form-control'>
  <option value='travail'>travail</option>
  <option value='courses' selected>courses</option>
  <option value='sante'>sante</option>
  <option value='famille'>familliale</option>
  <option value='sport'>sport / ballade</option>
  <option value='judiciaire'>judiciaire</option>
  <option value='missions'>missions</option>
    </select>
  </div>
  <div class="form-group col-md-6">
    <label for="profils">Profils:</label>
    <select size='5' id='profils' class='form-control'>
      <option selected>Choose...</option>
    </select>
  </div>
  </div>

  <div class="form-row">
  <div class="form-group col-md-6 text-center">
    <button type='submit' id='save'   class="btn btn-success">save profil</button>
    <button type='submit' id='delete' class="btn btn-danger">delete profil</button>
  </div>

  <div class="form-group col-md-6 text-center">
    <button type='submit' id='url' class="btn btn-secondary">make url</button>
    <button type='submit' id='gen' class="btn btn-primary">generate pdf</button>
  </div>
</form>

<span id='url'></span>
