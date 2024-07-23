describe('GestionSoutien', () => {
  beforeEach(() => {
    cy.visit('http://localhost:8000/');
    cy.get('form').find('input[name="username"]').type('p001');
    cy.get('form').find('input[name="password"]').type('p001@2023');
    cy.get('button[type="submit"]').contains('Se connecter').click();
    cy.url().should('include', '/accueil');
    cy.get('a.nav-link').contains('Suivi').click();
    cy.url().should('include', '/suivi/suivi_general');
  });
  it('prof - suivi - first week (all uncheck)', () => {
    cy.get('select#selec-sem').select('1');
    cy.get('div#grps_filtres')
      .find('input[type="checkbox"][value="GroupeA"]')
      .uncheck();
    cy.get('div#grps_filtres')
      .find('input[type="checkbox"][value="GroupeB"]')
      .uncheck();
    cy.get('div#grps_filtres')
      .find('input[type="checkbox"][value="GroupeC"]')
      .uncheck();
    cy.get('div#grps_filtres')
      .find('input[type="checkbox"][value="GroupeD"]')
      .uncheck();
    cy.get('input[type="submit"]#liaison_bd').contains('Valider').click();
    cy.get('table')
      .find('th')
      .contains('Suivi Etudiant')
      .should('have.length.greaterThan', 0);
    cy.get('tbody').find('tr').should('have.length.greaterThan', 0);
  });
  it('prof - suivi - first week (GroupeA check only)', function () {
    cy.get('select#selec-sem').select('1');
    cy.get('div#grps_filtres')
      .find('input[type="checkbox"][value="GroupeA"]')
      .check();
    cy.get('div#grps_filtres')
      .find('input[type="checkbox"][value="GroupeB"]')
      .uncheck();
    cy.get('div#grps_filtres')
      .find('input[type="checkbox"][value="GroupeC"]')
      .uncheck();
    cy.get('div#grps_filtres')
      .find('input[type="checkbox"][value="GroupeD"]')
      .uncheck();
    cy.get('input[type="submit"]#liaison_bd').contains('Valider').click();
    cy.get('table')
      .find('th')
      .contains('Suivi Etudiant')
      .should('have.length.greaterThan', 0);
    cy.get('tbody').find('tr').should('have.length.greaterThan', 0);
    cy.get('tbody').find('tr').first().invoke('text').as('firstRowData');
    cy.get('tbody tr:first-child td#eleve_groupe').should('contain', 'GroupeA');
  });
  it('prof - suivi - first week (GroupeB check only)', function () {
    cy.get('select#selec-sem').select('1');
    cy.get('div#grps_filtres')
      .find('input[type="checkbox"][value="GroupeA"]')
      .uncheck();
    cy.get('div#grps_filtres')
      .find('input[type="checkbox"][value="GroupeB"]')
      .check();
    cy.get('div#grps_filtres')
      .find('input[type="checkbox"][value="GroupeC"]')
      .uncheck();
    cy.get('div#grps_filtres')
      .find('input[type="checkbox"][value="GroupeD"]')
      .uncheck();
    cy.get('input[type="submit"]#liaison_bd').contains('Valider').click();
    cy.get('table')
      .find('th')
      .contains('Suivi Etudiant')
      .should('have.length.greaterThan', 0);
    cy.get('tbody').find('tr').should('have.length.greaterThan', 0);
    cy.get('tbody')
      .find('tr')
      .first()
      .invoke('text')
      .should('not.eq', this.firstRowData);
    cy.get('tbody tr:first-child td#eleve_groupe').should('contain', 'GroupeB');
  });
  it('prof - suivi - first week (GroupeC check only)', function () {
    cy.get('select#selec-sem').select('1');
    cy.get('div#grps_filtres')
      .find('input[type="checkbox"][value="GroupeA"]')
      .uncheck();
    cy.get('div#grps_filtres')
      .find('input[type="checkbox"][value="GroupeB"]')
      .uncheck();
    cy.get('div#grps_filtres')
      .find('input[type="checkbox"][value="GroupeC"]')
      .check();
    cy.get('div#grps_filtres')
      .find('input[type="checkbox"][value="GroupeD"]')
      .uncheck();
    cy.get('input[type="submit"]#liaison_bd').contains('Valider').click();
    cy.get('table')
      .find('th')
      .contains('Suivi Etudiant')
      .should('have.length.greaterThan', 0);
    cy.get('tbody').find('tr').should('have.length.greaterThan', 0);
    cy.get('tbody')
      .find('tr')
      .first()
      .invoke('text')
      .should('not.eq', this.firstRowData);
    cy.get('tbody tr:first-child td#eleve_groupe').should('contain', 'GroupeC');
  });
  it('prof - suivi - first week (GroupeD check only)', function () {
    cy.get('select#selec-sem').select('1');
    cy.get('div#grps_filtres')
      .find('input[type="checkbox"][value="GroupeA"]')
      .uncheck();
    cy.get('div#grps_filtres')
      .find('input[type="checkbox"][value="GroupeB"]')
      .uncheck();
    cy.get('div#grps_filtres')
      .find('input[type="checkbox"][value="GroupeC"]')
      .uncheck();
    cy.get('div#grps_filtres')
      .find('input[type="checkbox"][value="GroupeD"]')
      .check();
    cy.get('input[type="submit"]#liaison_bd').contains('Valider').click();
    cy.get('table')
      .find('th')
      .contains('Suivi Etudiant')
      .should('have.length.greaterThan', 0);
    cy.get('tbody').find('tr').should('have.length.greaterThan', 0);
    cy.get('tbody')
      .find('tr')
      .first()
      .invoke('text')
      .should('not.eq', this.firstRowData);
    cy.get('tbody tr:first-child td#eleve_groupe').should('contain', 'GroupeD');
  });
  it('prof - suivi - compare two differents week', function () {
    cy.get('select#selec-sem').select('1');
    cy.get('div#grps_filtres')
      .find('input[type="checkbox"][value="GroupeA"]')
      .uncheck();
    cy.get('div#grps_filtres')
      .find('input[type="checkbox"][value="GroupeB"]')
      .uncheck();
    cy.get('div#grps_filtres')
      .find('input[type="checkbox"][value="GroupeC"]')
      .uncheck();
    cy.get('div#grps_filtres')
      .find('input[type="checkbox"][value="GroupeD"]')
      .uncheck();
    cy.get('input[type="submit"]#liaison_bd').contains('Valider').click();
    cy.get('table')
      .find('th')
      .contains('Suivi Etudiant')
      .should('have.length.greaterThan', 0);
    cy.get('tbody').find('tr').should('have.length.greaterThan', 0);
    cy.get('tbody').find('tr').first().invoke('text').as('firstRowData2');
    cy.get('select#selec-sem').select('2');
    cy.get('div#grps_filtres')
      .find('input[type="checkbox"][value="GroupeA"]')
      .uncheck();
    cy.get('div#grps_filtres')
      .find('input[type="checkbox"][value="GroupeB"]')
      .uncheck();
    cy.get('div#grps_filtres')
      .find('input[type="checkbox"][value="GroupeC"]')
      .uncheck();
    cy.get('div#grps_filtres')
      .find('input[type="checkbox"][value="GroupeD"]')
      .uncheck();
    cy.get('input[type="submit"]#liaison_bd').contains('Valider').click();
    cy.get('table')
      .find('th')
      .contains('Suivi Etudiant')
      .should('have.length.greaterThan', 0);
    cy.get('tbody').find('tr').should('have.length.greaterThan', 0);
    cy.get('tbody')
      .find('tr')
      .first()
      .invoke('text')
      .should('not.eq', this.firstRowData2);
  });
});
