counter=1
$(document).ready(function() {
    var newIngredient = $("<input required  placeholder='Ingredient' type='text' value=''></input>")
        .attr("id", "ingredients-"+counter)
        .attr("name", "ingredients-"+counter)
    $("#ingredients").append(newIngredient)
    counter=counter+1

    var newIngredientQuantity = $("<input  placeholder='Quantity' required type='text' value=''></input>")
            .attr("id", "ingredients-"+counter)
            .attr("name", "ingredients-"+counter)
    $("#ingredients").append(newIngredientQuantity)
    counter=counter+1
$("#addNewIngredientField").click(function() {
    var newIngredient = $("<input required   type='text' value=''></input>")
        .attr("id", "ingredients-"+counter)
        .attr("name", "ingredients-"+counter)
    $("#ingredients").append(newIngredient)
    counter=counter+1

    var newIngredientQuantity = $("<input  required type='text' value=''></input>")
            .attr("id", "ingredients-"+counter)
            .attr("name", "ingredients-"+counter)
    $("#ingredients").append(newIngredientQuantity)
    counter=counter+1
});
});

