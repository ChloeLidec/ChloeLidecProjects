describe('GestionSoutien', () => {
  beforeEach(() => {
    cy.visit('http://localhost:8000/');
    cy.get('form').find('input[name="username"]').type('root');
    cy.get('form').find('input[name="password"]').type('root');
    cy.get('button[type="submit"]').contains('Se connecter').click();
    cy.url().should('include', '/accueil');
  });
  it('root - soutien - check data in table', () => {
    cy.get('a.nav-link').contains('Soutien').click();
    cy.url().should('include', '/soutien/');
    cy.get('select[name="semaine"]').select('1');
    cy.get('input[type="submit"]').contains('Valider').click();
    cy.get('table')
      .find('th')
      .contains('Soutiens de la semaine')
      .should('have.length.greaterThan', 0);
    cy.get('tbody').find('tr').should('have.length.greaterThan', 0);
  });
  it('root - soutien - change commentary', () => {
    cy.get('a.nav-link').contains('Soutien').click();
    cy.url().should('include', '/soutien/');
    cy.get('select[name="semaine"]').select('1');
    cy.get('input[type="submit"]').contains('Valider').click();
    cy.get('table')
      .find('th')
      .contains('Soutiens de la semaine')
      .should('have.length.greaterThan', 0);
    cy.get('tbody').find('tr').should('have.length.greaterThan', 0);
    cy.get('tbody').find('tr').first().invoke('text').as('firstRowData');
    cy.get('tbody').find('tr').first().find('td.date').should('not.be.empty');
    cy.get('tbody').find('tr').first().find('textarea[name="commval"]').click();
    cy.get('tbody').find('tr').first().find('textarea[name="commval"]').clear();
    cy.get('tbody')
      .find('tr')
      .first()
      .find('textarea[name="commval"]')
      .type('test');
    cy.get('tbody')
      .find('tr')
      .first()
      .find('textarea[name="commval"]')
      .should('have.value', 'test');
    cy.get('input[type="submit"]').contains('Sauvegarder commentaires').click();
    cy.reload();
    cy.get('tbody')
      .find('tr')
      .first()
      .find('textarea[name="commval"]')
      .should('have.value', 'test');
  });
});
