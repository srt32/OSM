class Call < ActiveRecord::Base
  attr_accessible :API_response_filename, :DP_DB_filename, :DP_rails_filename, :school_data_filename, :school_name, :script_name
end
