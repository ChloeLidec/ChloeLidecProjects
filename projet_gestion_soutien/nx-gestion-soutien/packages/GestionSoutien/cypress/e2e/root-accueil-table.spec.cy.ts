describe('GestionSoutien', () => {
  beforeEach(() => {
    cy.visit('http://localhost:8000/');
    cy.get('form').find('input[name="username"]').type('root');
    cy.get('form').find('input[name="password"]').type('root');
    cy.get('button[type="submit"]').contains('Se connecter').click();
    cy.url().should('include', '/accueil');
  });
  it('root - accueil - show data table', () => {
    // Custom command example, see `../support/commands.ts` file
    cy.get('table')
      .find('tr')
      .contains('Resultats sondages')
      .should('have.length.greaterThan', 0);
  });
});
