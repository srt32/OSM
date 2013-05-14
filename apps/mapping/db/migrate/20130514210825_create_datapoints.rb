class CreateDatapoints < ActiveRecord::Migration
  def change
    create_table :datapoints do |t|
      t.text :name
      t.float :latitude
      t.float :longitude
      t.boolean :gmaps

      t.timestamps
    end
  end
end
