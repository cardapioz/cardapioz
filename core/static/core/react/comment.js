var CommentList = React.createClass({
    getInitialState: function () {
        return { lista: []}
    },

    componentDidMount() {
        $.ajax({
            url: 'http://127.0.0.1:8000/comments/2',
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
            <ul className={'collection'}>
                { this.state.lista.map(function (comment) {
                    return (
                        <li key={comment.id} className="collection-item">
                            <span className="title">{ comment.user.get_full_name }</span>
                            <p className="">{ comment.comment_text }</p>
                            <a className="comment-date secondary-content grey-text text-lighten-1">{ comment.data_published }</a>
                        </li>
                    )
                })
                }
            </ul>
        );
    }
});

ReactDOM.render(
    <CommentList />,
    document.getElementById('collection')
);

