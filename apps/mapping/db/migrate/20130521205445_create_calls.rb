class CreateCalls < ActiveRecord::Migration
  def change
    create_table :calls do |t|
      t.string :script_name
      t.string :school_data_filename
      t.string :school_name
      t.string :API_response_filename
      t.string :DP_rails_filename
      t.string :DP_DB_filename

      t.timestamps
    end
  end
end
