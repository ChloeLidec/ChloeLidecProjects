describe('GestionSoutien', () => {
  const matieresATester = [
    'Modélisation',
    'Architecture réseaux',
    "Systèmes d'exploitation",
    'Développement web',
    'Intelligence artificielle',
  ];

  beforeEach(() => {
    cy.visit('http://localhost:8000/');
    cy.get('form').find('input[name="username"]').type('root');
    cy.get('form').find('input[name="password"]').type('root');
    cy.get('button[type="submit"]').contains('Se connecter').click();
    cy.url().should('include', '/accueil');
    cy.get('a.nav-link').contains('Disponibilites vue').click();
    cy.url().should('include', '/disponibilites/vue/');
  });
  
  matieresATester.forEach((matiere) => {
    it(`root - disponibilite - first week (${matiere} check)`, () => {
      cy.get('select#selec-sem').select('1');
      cy.get('#grps_filtres input[type="checkbox"]').uncheck();
      cy.get(
        `#grps_filtres input[type="checkbox"][value="${matiere}"]`
      ).check();
      cy.get('input[type="submit"]#liaison_bd').contains('Valider').click();
      cy.get('table')
        .find('th')
        .contains('Disponibilités')
        .should('have.length.greaterThan', 0);
      cy.get('tbody').find('tr').should('have.length.greaterThan', 0);
      cy.get('thead th').should('contain', matiere);
    });
  });
});
