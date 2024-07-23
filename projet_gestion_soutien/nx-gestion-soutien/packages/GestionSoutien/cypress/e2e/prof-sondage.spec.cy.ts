describe('GestionSoutien', () => {
  beforeEach(() => {
    cy.visit('http://localhost:8000/');
    cy.get('form').find('input[name="username"]').type('p001');
    cy.get('form').find('input[name="password"]').type('p001@2023');
    cy.get('button[type="submit"]').contains('Se connecter').click();
    cy.url().should('include', '/accueil');
    cy.get('a.nav-link').contains('Sondage').click();
    cy.url().should('include', '/sondages');
  });
  it('prof - sondage - first week (all uncheck)', () => {
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
      .contains('Sondage')
      .should('have.length.greaterThan', 0);
    cy.get('tbody').find('tr').should('have.length.greaterThan', 0);
  });
  it('prof - sondage - first week (GroupeA check only)', function () {
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
    cy.get('table').find('th').contains('Sondage');
    cy.get('tbody').find('tr').should('have.length.greaterThan', 0);
    cy.get('tbody').find('tr').first().invoke('text').as('firstRowData');
    cy.get('tbody tr:first-child td#eleve_groupe').should('contain', 'GroupeA');
  });
  it('prof - sondage - first week (GroupeB check only)', function () {
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
      .contains('Sondage')
      .should('have.length.greaterThan', 0);
    cy.get('tbody').find('tr').should('have.length.greaterThan', 0);
    cy.get('tbody')
      .find('tr')
      .first()
      .invoke('text')
      .should('not.eq', this.firstRowData);
    cy.get('tbody tr:first-child td#eleve_groupe').should('contain', 'GroupeB');
  });
  it('prof - sondage - first week (GroupeC check only)', function () {
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
      .contains('Sondage')
      .should('have.length.greaterThan', 0);
    cy.get('tbody').find('tr').should('have.length.greaterThan', 0);
    cy.get('tbody')
      .find('tr')
      .first()
      .invoke('text')
      .should('not.eq', this.firstRowData);
    cy.get('tbody tr:first-child td#eleve_groupe').should('contain', 'GroupeC');
  });
  it('prof - sondage - first week (GroupeD check only)', function () {
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
      .contains('Sondage')
      .should('have.length.greaterThan', 0);
    cy.get('tbody').find('tr').should('have.length.greaterThan', 0);
    cy.get('tbody')
      .find('tr')
      .first()
      .invoke('text')
      .should('not.eq', this.firstRowData);
    cy.get('tbody tr:first-child td#eleve_groupe').should('contain', 'GroupeD');
  });
  it('prof - sondage - compare two differents week', function () {
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
      .contains('Sondage')
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
      .contains('Sondage')
      .should('have.length.greaterThan', 0);
    cy.get('tbody').find('tr').should('have.length.greaterThan', 0);
    cy.get('tbody')
      .find('tr')
      .first()
      .invoke('text')
      .should('not.eq', this.firstRowData2);
  });
  it('prof - sondage - compare two differents groups (A-B) (first week)', function () {
    cy.get('select#selec-sem').select('1');
    cy.get('div#grps_filtres')
      .find('input[type="checkbox"][value="GroupeA"]')
      .check();
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
      .contains('Sondage')
      .should('have.length.greaterThan', 0);
    cy.get('tbody').find('tr').should('have.length.greaterThan', 0);
    cy.get('tbody tr')
      .should('have.length.greaterThan', 0)
      .and('satisfy', ($rows) => {
        return Cypress.$.makeArray($rows).every((row) => {
          const text = Cypress.$(row).find('td#eleve_groupe').text();
          return text.includes('GroupeA') || text.includes('GroupeB');
        });
      });
  });
});
