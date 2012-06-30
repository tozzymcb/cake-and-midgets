$(document).ready(function() {

	$('#comment').hide();
	if($('#comment')) {
		$('#leave_a_comment').click(function(event) {
			$('#comment').slideDown();
			event.preventDefault();
		});
	}

});
