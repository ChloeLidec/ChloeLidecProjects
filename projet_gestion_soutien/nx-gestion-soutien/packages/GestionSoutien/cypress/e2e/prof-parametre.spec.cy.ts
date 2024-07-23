describe('GestionSoutien', () => {
  // Faire une fonction qui permet de cocher toutes les checkbox
  function cocherTousLesCheckbox() {
    cy.get('input[type="checkbox"]').check();
  }

  // Faire une fonction qui permet de décocher toutes les checkbox
  function decocherTousLesCheckbox() {
    cy.get('input[type="checkbox"]').uncheck();
  }
  // Faire une fonction qui permet de vérifier que toutes les checkbox sont cochées
  function verifierQueTousLesCheckboxSontCoches() {
    cy.get('input[type="checkbox"]').should('be.checked');
  }
  // Faire une fonction qui permet de vérifier que toutes les checkbox sont décochées
  function verifierQueTousLesCheckboxSontDecoches() {
    cy.get('input[type="checkbox"]').should('not.be.checked');
  }

  beforeEach(() => {
    cy.visit('http://localhost:8000/');
    cy.get('form').find('input[name="username"]').type('p001');
    cy.get('form').find('input[name="password"]').type('p001@2023');
    cy.get('button[type="submit"]').contains('Se connecter').click();
    cy.url().should('include', '/accueil');
    cy.get('a.nav-link').contains('Parametres').click();
    cy.url().should('include', '/parametres/');
  });
  it('prof - parametres - check all save', () => {
    cocherTousLesCheckbox();
    verifierQueTousLesCheckboxSontCoches();
    cy.get('input[type="submit"]')
      .contains('Sauvegarder les modifications')
      .click();
    cy.reload();
    verifierQueTousLesCheckboxSontCoches();
  });
  it('prof - parametres - uncheck all save', () => {
    decocherTousLesCheckbox();
    verifierQueTousLesCheckboxSontDecoches();
    cy.get('input[type="submit"]')
      .contains('Sauvegarder les modifications')
      .click();
    cy.reload();
    verifierQueTousLesCheckboxSontDecoches();
  });

  it('prof - parametres - check all save 2', () => {
    cocherTousLesCheckbox();
    verifierQueTousLesCheckboxSontCoches();
    cy.get('input[type="submit"]')
      .contains('Sauvegarder les modifications')
      .click();
  });
});
