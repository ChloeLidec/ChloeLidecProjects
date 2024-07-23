describe('GestionSoutien', () => {
  beforeEach(() => {
    cy.visit('http://localhost:8000/');
    // Besoins de se connecter en tant que root pour pouvoir créer un soutien automatiquement
    cy.get('form').find('input[name="username"]').type('root');
    cy.get('form').find('input[name="password"]').type('root');
    cy.get('button[type="submit"]').contains('Se connecter').click();
    cy.url().should('include', '/accueil');
    cy.get('a.nav-link').contains('Déconnexion').click();
    cy.url().should('include', '/user/logout/');

    // Ensuite on se connecte en tant que prof
    cy.get('form').find('input[name="username"]').type('p001');
    cy.get('form').find('input[name="password"]').type('p001@2023');
    cy.get('button[type="submit"]').contains('Se connecter').click();
    cy.url().should('include', '/accueil');
    cy.get('a.nav-link').contains('Disponibilites gerer').click();
    cy.url().should('include', '/disponibilites/gerer/');
  });
  it(`prof - disponibilite - check date/week`, () => {
    // Récupérer qu'il y ai un bouton
    if (cy.get('button[type="submit"]').contains("S'inscrire")) {
      cy.get('button').contains("S'inscrire").click();
      cy.get('a.nav-link').contains('Déconnexion').click();
      cy.url().should('include', '/user/logout/');
      cy.get('form').find('input[name="username"]').type('root');
      cy.get('form').find('input[name="password"]').type('root');
      cy.get('button[type="submit"]').contains('Se connecter').click();
      cy.url().should('include', '/accueil');
      cy.get('a.nav-link').contains('Disponibilites vue').click();
      cy.url().should('include', '/disponibilites/vue/');
      cy.get('table')
        .find('th')
        .contains('Disponibilités')
        .should('have.length.greaterThan', 0);
      cy.get('tbody').find('tr').should('have.length.greaterThan', 0);
      cy.get('tbody').find('tr').first().invoke('text').as('firstRowData');
      cy.get('tbody').find('tr').first().find('td.date').should('not.be.empty');
      cy.get('a.nav-link').contains('Déconnexion').click();
      cy.url().should('include', '/user/logout/');
    } else {
      cy.get('a.nav-link').contains('Déconnexion').click();
      cy.url().should('include', '/user/logout/');
      cy.get('form').find('input[name="username"]').type('root');
      cy.get('form').find('input[name="password"]').type('root');
      cy.get('button[type="submit"]').contains('Se connecter').click();
      cy.url().should('include', '/accueil');
      cy.get('a.nav-link').contains('Disponibilites vue').click();
      cy.url().should('include', '/disponibilites/vue/');
      cy.get('table')
        .find('th')
        .contains('Disponibilités')
        .should('have.length.greaterThan', 0);
      cy.get('tbody').find('tr').should('have.length.greaterThan', 0);
      cy.get('tbody').find('tr').first().invoke('text').as('firstRowData');
      cy.get('tbody').find('tr').first().find('td.date').should('not.be.empty');
      cy.get('a.nav-link').contains('Déconnexion').click();
      cy.url().should('include', '/user/logout/');
    }
  });
});
