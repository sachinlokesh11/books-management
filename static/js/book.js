$(document).ready(function () {
	
    $('#datatables').DataTable({
		data: JSON.parse('{{ books|escapejs }}')
	});
});