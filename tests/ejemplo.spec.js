const { test, expect } = require('@playwright/test');

test('Verificar que la API de Películas responde', async ({ page }) => {
  // Navega a la aplicacion
  await page.goto('http://localhost:8000' ); 

  // el JSON devolveria {"message": "API de Películas funcionando"}
  const body = await page.locator('body');
  await expect(body).toContainText('API de Películas funcionando');
});

test('Simular Login de Administrador', async ({ page }) => {
  await page.goto('http://localhost:8000/docs' ); 
  await expect(page).toHaveTitle(/Swagger UI/);
});
