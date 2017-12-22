var Order = React.createClass({
    getInitialState: function () {
        return {
            id: 61,
            product: 2,
            client: 1,
            deliver_on: 1,
            note: '',
            amount: 1,
            payment: 0
        }
    },

    componentDidMount() {
        $.ajax({
            url: '/pedir/',
            //url: 'http://cdc-react.herokuapp.com/api/autores/',
            datatype: 'json',
            cache: false,
            success: function (resposta) {
                this.setState({lista: resposta})
            }.bind(this)
        });
    },

    render: function () {
        return(
            <div>a</div>
        );
    }
});

ReactDOM.render(
    <Order />,
    document.getElementById('')
);

