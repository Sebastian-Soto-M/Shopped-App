counter=1
$(document).ready(function() {
    var newIngredient = $("<input required  placeholder='Ingredient' type='text' value=''></input>")
        .attr("id", "ingredients-"+counter)
        .attr("name", "ingredients-"+counter)
    $("#ingredients").append(newIngredient)
    var newIngredientQuantity = $("<input  placeholder='Quantity' required type='text' value=''></input>")
            .attr("id", "ingredients-q-"+counter)
            .attr("name", "ingredients-q-"+counter)
    $("#ingredients").append(newIngredientQuantity)
    counter=counter+1
$("#addNewIngredientField").click(function() {
    var newIngredient = $("<div style='display: inline-block'><input required class='form-control'  type='text' value=''></input></div>")
        .attr("id", "ingredient"+counter)
        .attr("name", "ingredient"+counter)
    $("#ingredients").append(newIngredient)
    var newIngredientQuantity = $("<div style='display: inline-block'><input class='form-control'  required type='text' value=''></input></div>")
            .attr("id", "ingredientQuantity"+counter)
            .attr("name", "ingredientQuantity"+counter)
    $("#ingredients").append(newIngredientQuantity)
    counter=counter+1
});
});

