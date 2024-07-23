describe('GestionSoutien', () => {
  beforeEach(() => {
    cy.visit('http://localhost:8000/');
  });
  it('root - login', () => {
    // Custom command example, see `../support/commands.ts` file
    cy.get('form').find('input[name="username"]').type('root');
    cy.get('form').find('input[name="password"]').type('root');
    cy.get('button[type="submit"]').contains('Se connecter').click();
    cy.url().should('include', '/accueil');
  });
});
