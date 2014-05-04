import os
from node_start_api import PersonalAssistantTask as BaseTask

CREATE_ROUTE = """
exports.create = function ( req, res ) {

    async.waterfall( [
        function ( callback ) {
            ValidationManager.create( req.body, callback );
        },
        function ( validationResult, callback ) {
            DataManager.create( validationResult, callback );
        }
    ], function ( err, dataForResponse ) {
        if ( err ) {
            return utils.handleRouteError( err, res );
        }
        return res.json( dataForResponse, 201 );
    } );

};
"""


class PersonalAssistantTask(BaseTask):

    def prepare_index_file(self, index_file):
        super(PersonalAssistantTask, self).prepare_index_file(index_file)
        index_file.write("\n")
        index_file.write(CREATE_ROUTE)
        index_file.write("\n")
