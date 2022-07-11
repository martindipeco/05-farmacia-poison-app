// Run Script once DOM is loaded
document.addEventListener("DOMContentLoaded", function()
{
    // Validating password match
    document.querySelector("#check").addEventListener("click", function()
    {
        let input1 = document.querySelector("#pass1");
        let input2 = document.querySelector("#pass2");
        if (input1 == input2)
        {
            document.querySelector("#feedback").innerHTML = "Correcto";
        }
        else
        {
            input2.style.backgroundColor = "red";
            document.querySelector("#feedback").innerHTML = "No coinciden";
        }
    });
});