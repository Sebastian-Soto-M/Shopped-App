counter=1
$(document).ready(function() {
    var newIngredient = $("<div style='display: inline-block'><input required  placeholder='Ingredient' type='text' value=''></input></div>")
        .attr("id", "ingredient"+counter)
        .attr("name", "ingredient"+counter)
    $("#flist").append(newIngredient)
    var newIngredientQuantity = $("<div style='display: inline-block'><input  placeholder='Quantity' required type='text' value=''></input></div>")
            .attr("id", "ingredientQuantity"+counter)
            .attr("name", "ingredientQuantity"+counter)
    $("#flist").append(newIngredientQuantity)
    counter=counter+1
$("#addNewIngredientField").click(function() {
    var newIngredient = $("<div style='display: inline-block'><input required class='form-control' placeholder='Ingredient' type='text' value=''></input></div>")
        .attr("id", "ingredient"+counter)
        .attr("name", "ingredient"+counter)
    $("#flist").append(newIngredient)
    var newIngredientQuantity = $("<div style='display: inline-block'><input class='form-control' placeholder='Quantity' required type='text' value=''></input></div>")
            .attr("id", "ingredientQuantity"+counter)
            .attr("name", "ingredientQuantity"+counter)
    $("#flist").append(newIngredientQuantity)
    counter=counter+1
});
});

