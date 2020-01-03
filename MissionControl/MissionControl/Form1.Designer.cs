namespace MissionControl
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.tb_lat = new System.Windows.Forms.TextBox();
            this.tb_long = new System.Windows.Forms.TextBox();
            this.lab_lat = new System.Windows.Forms.Label();
            this.lab_long = new System.Windows.Forms.Label();
            this.tb_raw = new System.Windows.Forms.TextBox();
            this.btn_fix = new System.Windows.Forms.RadioButton();
            this.map = new GMap.NET.WindowsForms.GMapControl();
            this.btn_data_save = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // tb_lat
            // 
            this.tb_lat.Location = new System.Drawing.Point(97, 54);
            this.tb_lat.Name = "tb_lat";
            this.tb_lat.ReadOnly = true;
            this.tb_lat.Size = new System.Drawing.Size(120, 20);
            this.tb_lat.TabIndex = 1;
            // 
            // tb_long
            // 
            this.tb_long.Location = new System.Drawing.Point(97, 97);
            this.tb_long.Name = "tb_long";
            this.tb_long.ReadOnly = true;
            this.tb_long.Size = new System.Drawing.Size(120, 20);
            this.tb_long.TabIndex = 2;
            // 
            // lab_lat
            // 
            this.lab_lat.AutoSize = true;
            this.lab_lat.Location = new System.Drawing.Point(15, 54);
            this.lab_lat.Name = "lab_lat";
            this.lab_lat.Size = new System.Drawing.Size(45, 13);
            this.lab_lat.TabIndex = 5;
            this.lab_lat.Text = "Latitude";
            // 
            // lab_long
            // 
            this.lab_long.AutoSize = true;
            this.lab_long.Location = new System.Drawing.Point(12, 97);
            this.lab_long.Name = "lab_long";
            this.lab_long.Size = new System.Drawing.Size(54, 13);
            this.lab_long.TabIndex = 6;
            this.lab_long.Text = "Longitude";
            // 
            // tb_raw
            // 
            this.tb_raw.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.tb_raw.Location = new System.Drawing.Point(15, 12);
            this.tb_raw.Name = "tb_raw";
            this.tb_raw.ReadOnly = true;
            this.tb_raw.Size = new System.Drawing.Size(610, 20);
            this.tb_raw.TabIndex = 9;
            // 
            // btn_fix
            // 
            this.btn_fix.AutoSize = true;
            this.btn_fix.Location = new System.Drawing.Point(97, 141);
            this.btn_fix.Name = "btn_fix";
            this.btn_fix.Size = new System.Drawing.Size(38, 17);
            this.btn_fix.TabIndex = 10;
            this.btn_fix.TabStop = true;
            this.btn_fix.Text = "Fix";
            this.btn_fix.UseVisualStyleBackColor = true;
            // 
            // map
            // 
            this.map.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.map.Bearing = 0F;
            this.map.CanDragMap = true;
            this.map.EmptyTileColor = System.Drawing.Color.Navy;
            this.map.GrayScaleMode = false;
            this.map.HelperLineOption = GMap.NET.WindowsForms.HelperLineOptions.DontShow;
            this.map.LevelsKeepInMemory = 5;
            this.map.Location = new System.Drawing.Point(327, 54);
            this.map.MarkersEnabled = true;
            this.map.MaxZoom = 2;
            this.map.MinZoom = 2;
            this.map.MouseWheelZoomEnabled = true;
            this.map.MouseWheelZoomType = GMap.NET.MouseWheelZoomType.MousePositionAndCenter;
            this.map.Name = "map";
            this.map.NegativeMode = false;
            this.map.PolygonsEnabled = true;
            this.map.RetryLoadTile = 0;
            this.map.RoutesEnabled = true;
            this.map.ScaleMode = GMap.NET.WindowsForms.ScaleModes.Integer;
            this.map.SelectedAreaFillColor = System.Drawing.Color.FromArgb(((int)(((byte)(33)))), ((int)(((byte)(65)))), ((int)(((byte)(105)))), ((int)(((byte)(225)))));
            this.map.ShowTileGridLines = false;
            this.map.Size = new System.Drawing.Size(285, 239);
            this.map.TabIndex = 11;
            this.map.Zoom = 0D;
            // 
            // btn_data_save
            // 
            this.btn_data_save.Location = new System.Drawing.Point(97, 177);
            this.btn_data_save.Name = "btn_data_save";
            this.btn_data_save.Size = new System.Drawing.Size(120, 26);
            this.btn_data_save.TabIndex = 12;
            this.btn_data_save.Text = "Start Saving";
            this.btn_data_save.UseVisualStyleBackColor = true;
            this.btn_data_save.Click += new System.EventHandler(this.btn_data_save_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(637, 315);
            this.Controls.Add(this.btn_data_save);
            this.Controls.Add(this.map);
            this.Controls.Add(this.btn_fix);
            this.Controls.Add(this.tb_raw);
            this.Controls.Add(this.lab_long);
            this.Controls.Add(this.lab_lat);
            this.Controls.Add(this.tb_long);
            this.Controls.Add(this.tb_lat);
            this.Margin = new System.Windows.Forms.Padding(2);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.TextBox tb_lat;
        private System.Windows.Forms.TextBox tb_long;
        private System.Windows.Forms.Label lab_lat;
        private System.Windows.Forms.Label lab_long;
        private System.Windows.Forms.TextBox tb_raw;
        private System.Windows.Forms.RadioButton btn_fix;
        private GMap.NET.WindowsForms.GMapControl map;
        private System.Windows.Forms.Button btn_data_save;
    }
}

