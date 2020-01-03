namespace missionControl1
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
            this.map = new GMap.NET.WindowsForms.GMapControl();
            this.btn_fix = new System.Windows.Forms.RadioButton();
            this.tb_raw = new System.Windows.Forms.TextBox();
            this.tb_lat = new System.Windows.Forms.TextBox();
            this.tb_lon = new System.Windows.Forms.TextBox();
            this.btn_data_save = new System.Windows.Forms.Button();
            this.com_port = new System.Windows.Forms.ComboBox();
            this.SuspendLayout();
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
            this.map.Location = new System.Drawing.Point(335, 63);
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
            this.map.Size = new System.Drawing.Size(424, 375);
            this.map.TabIndex = 0;
            this.map.Zoom = 0D;
            // 
            // btn_fix
            // 
            this.btn_fix.AutoSize = true;
            this.btn_fix.Location = new System.Drawing.Point(71, 337);
            this.btn_fix.Name = "btn_fix";
            this.btn_fix.Size = new System.Drawing.Size(38, 17);
            this.btn_fix.TabIndex = 1;
            this.btn_fix.TabStop = true;
            this.btn_fix.Text = "Fix";
            this.btn_fix.UseVisualStyleBackColor = true;
            // 
            // tb_raw
            // 
            this.tb_raw.Location = new System.Drawing.Point(35, 16);
            this.tb_raw.Name = "tb_raw";
            this.tb_raw.ReadOnly = true;
            this.tb_raw.Size = new System.Drawing.Size(724, 20);
            this.tb_raw.TabIndex = 2;
            // 
            // tb_lat
            // 
            this.tb_lat.Location = new System.Drawing.Point(71, 252);
            this.tb_lat.Name = "tb_lat";
            this.tb_lat.ReadOnly = true;
            this.tb_lat.Size = new System.Drawing.Size(102, 20);
            this.tb_lat.TabIndex = 3;
            // 
            // tb_lon
            // 
            this.tb_lon.Location = new System.Drawing.Point(71, 301);
            this.tb_lon.Name = "tb_lon";
            this.tb_lon.ReadOnly = true;
            this.tb_lon.Size = new System.Drawing.Size(102, 20);
            this.tb_lon.TabIndex = 4;
            // 
            // btn_data_save
            // 
            this.btn_data_save.Location = new System.Drawing.Point(71, 360);
            this.btn_data_save.Name = "btn_data_save";
            this.btn_data_save.Size = new System.Drawing.Size(102, 21);
            this.btn_data_save.TabIndex = 5;
            this.btn_data_save.Text = "Start Saving";
            this.btn_data_save.UseVisualStyleBackColor = true;
            this.btn_data_save.Click += new System.EventHandler(this.btn_data_save_Click);
            // 
            // com_port
            // 
            this.com_port.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.com_port.FormattingEnabled = true;
            this.com_port.Location = new System.Drawing.Point(71, 128);
            this.com_port.Name = "com_port";
            this.com_port.Size = new System.Drawing.Size(121, 21);
            this.com_port.TabIndex = 6;
            this.com_port.SelectedIndexChanged += new System.EventHandler(this.comboBox1_SelectedIndexChanged);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(779, 450);
            this.Controls.Add(this.com_port);
            this.Controls.Add(this.btn_data_save);
            this.Controls.Add(this.tb_lon);
            this.Controls.Add(this.tb_lat);
            this.Controls.Add(this.tb_raw);
            this.Controls.Add(this.btn_fix);
            this.Controls.Add(this.map);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private GMap.NET.WindowsForms.GMapControl map;
        private System.Windows.Forms.RadioButton btn_fix;
        private System.Windows.Forms.TextBox tb_raw;
        private System.Windows.Forms.TextBox tb_lat;
        private System.Windows.Forms.TextBox tb_lon;
        private System.Windows.Forms.Button btn_data_save;
        private System.Windows.Forms.ComboBox com_port;
    }
}

