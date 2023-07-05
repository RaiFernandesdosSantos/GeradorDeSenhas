/**
 * Creates a custom header element with menu buttons.
 * @returns {HTMLElement} The custom header element.
 */
export function headerCustom() {
  // Create the header element
  const header = document.createElement("header");
  header.id = "header";

  // Create the menu header element
  const menuHeader = document.createElement("div");
  menuHeader.className = "menu-header";

  // Create and append the "Gerar Senha" button
  menuHeader.appendChild(
    createBtn({
      texto: "Gerar Senha",
      href: "../home/index.html",
    })
  );

  // Create and append the "Minhas Senhas" button
  menuHeader.appendChild(
    createBtn({
      texto: "Minhas Senhas",
      href: "../lista/index.html",
    })
  );

  // Append the menu header to the header element
  header.appendChild(menuHeader);

  // Return the custom header element
  return header;
}

/**
 * Creates a button element with a link inside.
 * - `props` is an object containing the properties of the button:
 *   - `texto`: the text content of the link.
 *   - `href`: the URL of the link.
 * @param {Object} props - The properties of the button.
 * @returns {Element} - The created button element.
 */
function createBtn(props) {
  // Create the button element
  const btn = document.createElement("div");
  btn.className = "btn";

  // Create the link element
  const link = document.createElement("a");
  link.className = "link-header-item";
  link.textContent = props.texto;
  link.href = props.href;

  // Append the link element to the button element
  btn.appendChild(link);

  // Return the created button element
  return btn;
}
