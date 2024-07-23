describe('GestionSoutien', () => {
  beforeEach(() => {
    cy.visit('http://localhost:8000/');
    cy.get('form').find('input[name="username"]').type('root');
    cy.get('form').find('input[name="password"]').type('root');
    cy.get('button[type="submit"]').contains('Se connecter').click();
    cy.url().should('include', '/accueil');
    cy.get('a.nav-link').contains('Résultat QCM').click();
    cy.url().should('include', '/qcm');
  });
  it('root - qcm - first week (all uncheck)', () => {
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
      .contains('QCM')
      .should('have.length.greaterThan', 0);
    cy.get('tbody').find('tr').should('have.length.greaterThan', 0);
  });
  it('root - qcm - first week (GroupeA check only)', function () {
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
      .contains('QCM')
      .should('have.length.greaterThan', 0);
    cy.get('tbody').find('tr').should('have.length.greaterThan', 0);
    cy.get('tbody').find('tr').first().invoke('text').as('firstRowData');
    cy.get('tbody tr:first-child td#eleve_groupe').should('contain', 'GroupeA');
  });
  it('root - qcm - first week (GroupeB check only)', function () {
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
      .contains('QCM')
      .should('have.length.greaterThan', 0);
    cy.get('tbody').find('tr').should('have.length.greaterThan', 0);
    cy.get('tbody')
      .find('tr')
      .first()
      .invoke('text')
      .should('not.eq', this.firstRowData);
    cy.get('tbody tr:first-child td#eleve_groupe').should('contain', 'GroupeB');
  });
  it('root - qcm - first week (GroupeC check only)', function () {
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
      .contains('QCM')
      .should('have.length.greaterThan', 0);
    cy.get('tbody').find('tr').should('have.length.greaterThan', 0);
    cy.get('tbody')
      .find('tr')
      .first()
      .invoke('text')
      .should('not.eq', this.firstRowData);
    cy.get('tbody tr:first-child td#eleve_groupe').should('contain', 'GroupeC');
  });
  it('root - qcm - first week (GroupeD check only)', function () {
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
      .contains('QCM')
      .should('have.length.greaterThan', 0);
    cy.get('tbody').find('tr').should('have.length.greaterThan', 0);
    cy.get('tbody')
      .find('tr')
      .first()
      .invoke('text')
      .should('not.eq', this.firstRowData);
    cy.get('tbody tr:first-child td#eleve_groupe').should('contain', 'GroupeD');
  });
  it('root - qcm - compare two differents week', function () {
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
      .contains('QCM')
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
      .contains('QCM')
      .should('have.length.greaterThan', 0);
    cy.get('tbody').find('tr').should('have.length.greaterThan', 0);
    cy.get('tbody')
      .find('tr')
      .first()
      .invoke('text')
      .should('not.eq', this.firstRowData2);
  });
  it('root - qcm - mean per group (first week - all uncheck)', () => {
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
      .contains('QCM')
      .should('have.length.greaterThan', 0);
    cy.get('tbody').find('tr').should('have.length.greaterThan', 0);
    cy.get('select').find('option[value="generale"]').click({ force: true });
    cy.get('thead')
      .find('tr')
      .find('th#moyenne_1')
      .invoke('text')
      .as('mean_g1');
    cy.get('thead')
      .find('tr')
      .find('th#moyenne_2')
      .invoke('text')
      .as('mean_g2');
    cy.get('select').find('option[value="GroupeA"]').click({ force: true });
    cy.get('thead')
      .find('tr')
      .find('th#moyenne_1')
      .invoke('text')
      .as('mean_a1');
    cy.get('thead')
      .find('tr')
      .find('th#moyenne_2')
      .invoke('text')
      .as('mean_a2');
    cy.get('@mean_g1').should('not.eq', this.mean_a1);
    cy.get('@mean_g2').should('not.eq', this.mean_a2);
  });
  it('root - qcm - compare two differents groups (A-B) (first week)', function () {
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
      .contains('QCM')
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
  it('root - qcm - redirect student link (first week - first student)', function () {
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
      .contains('QCM')
      .should('have.length.greaterThan', 0);
    cy.get('tbody').find('tr').should('have.length.greaterThan', 0);
    cy.get('tbody').find('tr').first().find('a').click();
  });
});
