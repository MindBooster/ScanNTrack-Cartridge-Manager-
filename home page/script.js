// Define variables for DOM elements
const navToggle = document.querySelector('.nav-toggle');
const navMenu = document.querySelector('.nav-menu');
const issueButton = document.querySelector('#issue-button');
const returnButton = document.querySelector('#return-button');
const returnForm = document.querySelector('#return-form');
const issueForm = document.querySelector('#issue-form');
const cartridgeModelSelect = document.querySelector('#cartridge-model-select');

// Add event listener for nav toggle button
navToggle.addEventListener('click', () => {
  navMenu.classList.toggle('nav-menu_visible');
});

// Add event listener for return button
returnButton.addEventListener('click', () => {
  // Show the return form and hide the issue form
  returnForm.style.display = 'block';
  issueForm.style.display = 'none';
});

// Add event listener for issue button
issueButton.addEventListener('click', () => {
  // Show the issue form and hide the return form
  issueForm.style.display = 'block';
  returnForm.style.display = 'none';
});

// Add event listener for cartridge model select in return form
cartridgeModelSelect.addEventListener('change', () => {
  // Update the input field for cartridge model in the form
  const selectedOption = cartridgeModelSelect.options[cartridgeModelSelect.selectedIndex];
  const cartridgeModelInput = document.querySelector('#return-cartridge-model');
  cartridgeModelInput.value = selectedOption.value;
});
