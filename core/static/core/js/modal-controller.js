function formaPagamento(){
	let inPayment = document.getElementsByName('payment');

	if(inPayment[0].checked) return 'em dinheiro';
	return 'no cartão';
}

function updateModal(modal){
	var D = document.querySelector.bind(document);

	var contentMsgPrimary = D('.pedido-msg-content-primary');
	var contentMsgSecond = D('.pedido-msg-content-second');
	var contentMsgThird = D('.pedido-msg-content-third');
	var contentMsgFourth = D('.pedido-msg-content-fourth');

	var modalFooter = D('.modal-footer-main');


	if(modal == 'confirmacao'){
		let inTotalCompra = D('.confirmacao-total-compra');
		let produtoPrice = D('.produto-price');
		let inQuantidade = D('#quantidade');
		let inLoc = D('#confirmacao-select');

		inTotalCompra.textContent = 'R$' + (produtoPrice.textContent * inQuantidade.value);
		contentMsgPrimary.textContent = inLoc.options[inLoc.selectedIndex].textContent + ' - ';
		contentMsgSecond.textContent = formaPagamento();
		contentMsgThird.textContent = '';
		contentMsgFourth.textContent = '';

		modalFooter.innerHTML = `
			<a href="#!" class="modal-action modal-close waves-effect waves-green btn-flat grey-text btn-footer-primary">cancelar</a>
            <a href="#!" class="modal-action modal-close waves-effect waves-green btn-flat teal-text darken-3 btn-footer-second" onclick="order_this()">Confirmar compra</a>
            `;

		$('#modal-main').modal('open');
	}
	else if(modal == 'pedido-ok'){
		let nameProduto = D('.nameProduto');
		let nameSaler = D('.title');

		contentMsgPrimary.textContent = 'Cardapioz e ';
		contentMsgSecond.textContent = nameSaler.textContent + 'agradecem sua compra.';
		contentMsgThird.textContent = nameProduto.textContent + ' chegará por volta de ';
		contentMsgFourth.textContent = '{ tempo estimado }';

		modalFooter.innerHTML = `
			<a href="#!" class="modal-action modal-close waves-effect waves-red btn-flat flow-text" style="font-size: 9pt; margin-right: : 0px; padding-right: -5px;">fechar</a>
            <a href="#!" class="modal-action modal-close waves-effect waves-green btn-flat flow-text  green-text" style="margin-left: : 0px; padding-left: -5px;">acompanhar pedido</a>
		`
		$('#modal-main').modal('open');
	}
}