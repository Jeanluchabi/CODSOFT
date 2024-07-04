document.addEventListener('DOMContentLoaded', function () {
    const display = document.getElementById('display');
    const buttons = Array.from(document.getElementsByClassName('btn'));

    let currentInput = '';
    let operator = null;
    let firstOperand = null;

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            const value = button.getAttribute('data-value');

            if (value === 'C') {
                currentInput = '';
                operator = null;
                firstOperand = null;
                display.innerText = '0';
            } else if (value === '=') {
                if (firstOperand !== null && operator !== null) {
                    currentInput = calculate(firstOperand, currentInput, operator);
                    display.innerText = currentInput;
                    operator = null;
                    firstOperand = null;
                }
            } else if (value === '√') {
                if (currentInput !== '') {
                    currentInput = Math.sqrt(parseFloat(currentInput)).toString();
                    display.innerText = currentInput;
                }
            } else if (['+', '-', '*', '/'].includes(value)) {
                if (currentInput !== '') {
                    if (firstOperand === null) {
                        firstOperand = currentInput;
                    } else {
                        firstOperand = calculate(firstOperand, currentInput, operator);
                    }
                    operator = value;
                    currentInput = '';
                }
            } else {
                if (value === '.' && currentInput.includes('.')) {
                    return;
                }
                currentInput += value;
                display.innerText = currentInput;
            }
        });
    });

    function calculate(first, second, operator) {
        const a = parseFloat(first);
        const b = parseFloat(second);

        if (operator === '+') return (a + b).toString();
        if (operator === '-') return (a - b).toString();
        if (operator === '*') return (a * b).toString();
        if (operator === '/') return (a / b).toString();
        return '';
    }
});
