describe('GestionSoutien', () => {
  beforeEach(() => {
    cy.visit('http://localhost:8000/');
  });
  it('prof - login', () => {
    // Custom command example, see `../support/commands.ts` file
    cy.get('form').find('input[name="username"]').type('p001');
    cy.get('form').find('input[name="password"]').type('p001@2023');
    cy.get('button[type="submit"]').contains('Se connecter').click();
    cy.url().should('include', '/accueil');
  });
});
