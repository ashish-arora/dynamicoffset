function cqProductChange()
{
    if($("#custom_product").val() > 0)
    {
        data = "query=ChangeCustomQuoteProduct&id_product="+$("#custom_product").val()
        $.ajax({
            type: "GET",
            url: 'includes/ajaxresponse.php',
            dataType: "text",
            data: data,
            success: function(msg){
                $("#custom_table").html(msg);
            }
        });
    }
    else
    {
        $("#custom_table").html("");
    }
}

function cqFieldOption(id)
{
    if(parseInt($("#field_"+id).val()) == -1)
        $("#div_custom_"+id).show()
    else
        $("#div_custom_"+id).hide()
}

function resetQuotesForm()
{
    document.getElementById('customquotes').reset();
    cqProductChange();
}

