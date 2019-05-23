import requests
from bs4 import BeautifulSoup
voicesHtml='''<body>
	<div id="alert"></div>
	<div id="download_block">
		
		<div id="slowDownloadHint" class="topHint" hidden="true">
			<div class="text">如果您的电脑中插件无法下载所有页面的媒体素材，请您重新安装。</div>
			<div class="close" id="slowDownloadHint_close">x</div>
		</div>
		<!-- <div class="bgLine"></div> -->
		<div id="multiple_download_block">
			<div class="title">
				<h2 id="multiple_download_block_title">已识别的媒体文件：</h2>
				<div class="iconDiv">
					<a id="help_link_options" class="iconButtonOptions" title="设置"></a>
					<a id="help_link_clear" class="iconButtonClear" title="清除列表"></a>
				</div>
		
				<div id="noYoutubeMessage" hidden="true">
					<span>由于谷歌网站政策，您无法下载。</span><br>
					<span>请不要发布负面评论，对于这个我们也无能为力。</span><br>
					<span>希望您能够理解，谢谢！</span>
				</div>
			
				<div id="download_item_container"><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/19F934CE-40DB-4E51-91CB-C9AF0DB918E9-8712-000007D683010F57.aac">19F934CE-40DB-4E51-91CB-C9AF0DB918E9-8712-000007D683010F57.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.22MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/9D00BCC5-8328-43A5-891F-AE63CA849983-8712-000007D635D86F9F.aac">9D00BCC5-8328-43A5-891F-AE63CA849983-8712-000007D635D86F9F.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.1MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/AF5C5CCA-CDD4-4D4C-8938-8B8D56CF9BDB-8712-000007F1C68F3479.aac">AF5C5CCA-CDD4-4D4C-8938-8B8D56CF9BDB-8712-000007F1C68F3479.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.12MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/71D8098D-C6E6-4BBE-BD64-2CD23B6CE88C-8712-000007F171ACA16A.aac">71D8098D-C6E6-4BBE-BD64-2CD23B6CE88C-8712-000007F171ACA16A.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.17MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/8D4D1F56-1350-4003-BD46-DEF51D457F61-8712-000007F12D69309F.aac">8D4D1F56-1350-4003-BD46-DEF51D457F61-8712-000007F12D69309F.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.19MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/3DEA0487-A1DC-43AC-A488-38F7A9A15CD5-8712-000007F0D74A75CF.aac">3DEA0487-A1DC-43AC-A488-38F7A9A15CD5-8712-000007F0D74A75CF.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.16MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/C4462A3A-FCAC-4424-8EA0-9420D15F1D59-8712-000007F05721AE9C.aac">C4462A3A-FCAC-4424-8EA0-9420D15F1D59-8712-000007F05721AE9C.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.12MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/684C19B1-CA69-44CF-9D83-BA7F0981E2C5-8712-000007EFBEA6AF40.aac">684C19B1-CA69-44CF-9D83-BA7F0981E2C5-8712-000007EFBEA6AF40.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.11MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/E9C136EA-8EF4-4D6E-A6F8-ECD29E8FDE79-8712-000007EF5B831D5B.aac">E9C136EA-8EF4-4D6E-A6F8-ECD29E8FDE79-8712-000007EF5B831D5B.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.18MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/CEA9BB55-169E-43C8-BC7B-A90B2FD378F1-8712-000007EF31EEA473.aac">CEA9BB55-169E-43C8-BC7B-A90B2FD378F1-8712-000007EF31EEA473.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.11MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/E80F4187-CAD3-4984-AB3A-078AD04AECEF-8712-000007EEFB1C75FA.aac">E80F4187-CAD3-4984-AB3A-078AD04AECEF-8712-000007EEFB1C75FA.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.15MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/ED283A88-DA38-42C0-B790-90E3031C4993-8712-000007EEB08D8E25.aac">ED283A88-DA38-42C0-B790-90E3031C4993-8712-000007EEB08D8E25.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.14MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/7BD534E1-611B-4676-B5C7-C5FF8BD6678A-8712-000007EE74D38D50.aac">7BD534E1-611B-4676-B5C7-C5FF8BD6678A-8712-000007EE74D38D50.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.17MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/A7408CCE-A5E0-423C-A239-4ABA150EC0B5-8712-000007EE366DF5F4.aac">A7408CCE-A5E0-423C-A239-4ABA150EC0B5-8712-000007EE366DF5F4.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.11MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/B0FD72E5-B18C-4BCE-B2AB-02FE0BDF8A5A-8712-000007EDCB302C78.aac">B0FD72E5-B18C-4BCE-B2AB-02FE0BDF8A5A-8712-000007EDCB302C78.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.12MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/FDFCDABF-EC47-424D-95A5-03403D42D503-8712-000007ED659B1E4E.aac">FDFCDABF-EC47-424D-95A5-03403D42D503-8712-000007ED659B1E4E.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.12MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/9FCC8302-1E4E-4B2C-BA57-44AD56714541-8712-000007ED2E7B4407.aac">9FCC8302-1E4E-4B2C-BA57-44AD56714541-8712-000007ED2E7B4407.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.16MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/850637ED-5929-42B4-B320-D86D91ED311E-8712-000007ECEBF55A49.aac">850637ED-5929-42B4-B320-D86D91ED311E-8712-000007ECEBF55A49.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.16MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/95320B86-C133-4067-986E-49242B844EFC-8712-000007EC9D8FAF57.aac">95320B86-C133-4067-986E-49242B844EFC-8712-000007EC9D8FAF57.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.21MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/8C4E0C68-510C-4B62-AAD5-13909A1C7805-8712-000007EC4D855655.aac">8C4E0C68-510C-4B62-AAD5-13909A1C7805-8712-000007EC4D855655.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.1MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/45C0E781-9AF4-4536-9A09-8B05204C79D8-8712-000007EBFEE896A6.aac">45C0E781-9AF4-4536-9A09-8B05204C79D8-8712-000007EBFEE896A6.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.11MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/08765E79-AA57-4308-A172-999C35659CBB-8712-000007EA7665A860.aac">08765E79-AA57-4308-A172-999C35659CBB-8712-000007EA7665A860.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.15MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/3C4A7D91-FF85-4385-97CB-281B2B9C15E7-8712-000007EA15052F6E.aac">3C4A7D91-FF85-4385-97CB-281B2B9C15E7-8712-000007EA15052F6E.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.16MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/1F3DD3E4-7F3B-4260-9146-3685B719DC50-8712-000007E9B7BE9D1B.aac">1F3DD3E4-7F3B-4260-9146-3685B719DC50-8712-000007E9B7BE9D1B.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.17MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/D3D17F0D-053E-4791-80EB-DF2164C70C6B-8712-000007E92A232243.aac">D3D17F0D-053E-4791-80EB-DF2164C70C6B-8712-000007E92A232243.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.15MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/746436F7-BCA6-4666-86B6-3C04B2B2D64A-8712-000007E8E489C5D1.aac">746436F7-BCA6-4666-86B6-3C04B2B2D64A-8712-000007E8E489C5D1.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.11MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/237F3CB1-4789-4CB8-9046-F5F2FF58424E-8712-000007E8B33566B5.aac">237F3CB1-4789-4CB8-9046-F5F2FF58424E-8712-000007E8B33566B5.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.14MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/458E3024-251A-41D2-9D50-D4B920B1B1FA-8712-000007E881CD5DB0.aac">458E3024-251A-41D2-9D50-D4B920B1B1FA-8712-000007E881CD5DB0.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.13MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/6F50EA05-AE0D-460F-8D94-95D5FC281B66-8712-000007E7EAED111B.aac">6F50EA05-AE0D-460F-8D94-95D5FC281B66-8712-000007E7EAED111B.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.17MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/20C5B0B4-020D-401E-B264-A171C3A878B1-8712-000007E78471A311.aac">20C5B0B4-020D-401E-B264-A171C3A878B1-8712-000007E78471A311.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.19MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/8DDC6EC3-FC0A-4799-AA18-A4D3ACFFE25C-8712-000007E63270962B.aac">8DDC6EC3-FC0A-4799-AA18-A4D3ACFFE25C-8712-000007E63270962B.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.22MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/805EEF4A-9A10-46B2-904B-62D185378060-8712-000007E5E46CE12B.aac">805EEF4A-9A10-46B2-904B-62D185378060-8712-000007E5E46CE12B.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.13MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/60642474-FC91-41F7-A4D2-D83E96526980-8712-000007E5564499CF.aac">60642474-FC91-41F7-A4D2-D83E96526980-8712-000007E5564499CF.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.13MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/6099470D-D183-420A-8A2B-DE07E5D5C244-8712-000007E50FF51B4D.aac">6099470D-D183-420A-8A2B-DE07E5D5C244-8712-000007E50FF51B4D.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.2MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/CE8AB8FE-2B0C-4BFD-B1A5-2C1A3665A669-8712-000007E4757F661A.aac">CE8AB8FE-2B0C-4BFD-B1A5-2C1A3665A669-8712-000007E4757F661A.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.13MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/AB17AD8D-43B6-473D-BDE2-DB959AC68E9E-8712-000007E40EE01B29.aac">AB17AD8D-43B6-473D-BDE2-DB959AC68E9E-8712-000007E40EE01B29.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.23MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/700E1587-03DC-4477-8906-284EF4F5CD35-8712-000007E3BE551787.aac">700E1587-03DC-4477-8906-284EF4F5CD35-8712-000007E3BE551787.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.15MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/C052D1AB-052D-4221-A8C2-DAF04CBEDFDC-8712-000007E372ADCB40.aac">C052D1AB-052D-4221-A8C2-DAF04CBEDFDC-8712-000007E372ADCB40.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.16MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/49B24009-D554-4412-94C4-D5CF8A484B65-8712-000007E2F98CFEEF.aac">49B24009-D554-4412-94C4-D5CF8A484B65-8712-000007E2F98CFEEF.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.11MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/ACACE10F-7A05-484B-BB1D-6DED8E7DDC37-8712-000007E28B348269.aac">ACACE10F-7A05-484B-BB1D-6DED8E7DDC37-8712-000007E28B348269.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.15MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/3B4FA843-6462-426E-8B1D-35EA98419B30-8712-000007E20DC9825F.aac">3B4FA843-6462-426E-8B1D-35EA98419B30-8712-000007E20DC9825F.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.15MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/D24867DD-25A2-4926-9E50-F6D1F700F882-8712-000007E1C2C15E7C.aac">D24867DD-25A2-4926-9E50-F6D1F700F882-8712-000007E1C2C15E7C.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.19MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/C4164F74-0070-4FA5-9F1D-782EA1DBB2D4-8712-000007E0FBC7CF80.aac">C4164F74-0070-4FA5-9F1D-782EA1DBB2D4-8712-000007E0FBC7CF80.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.2MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/E102080F-3099-416F-88E7-42EEEE02380D-8712-000007E0C9E6640D.aac">E102080F-3099-416F-88E7-42EEEE02380D-8712-000007E0C9E6640D.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.12MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/BE98ADFB-B709-492C-9C11-D49353E09D67-8712-000007E034FF90DD.aac">BE98ADFB-B709-492C-9C11-D49353E09D67-8712-000007E034FF90DD.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.18MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/5E709042-BCAE-455B-B617-E83FB32CA094-8712-000007DFCACCF24F.aac">5E709042-BCAE-455B-B617-E83FB32CA094-8712-000007DFCACCF24F.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.24MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/EFDAA409-70D8-452D-A1BF-CA301AB54F58-8712-000007DF7250FB5B.aac">EFDAA409-70D8-452D-A1BF-CA301AB54F58-8712-000007DF7250FB5B.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.1MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/32E4F0F9-4B13-46C0-8954-E0D80252DE0E-8712-000007DF24DF63EB.aac">32E4F0F9-4B13-46C0-8954-E0D80252DE0E-8712-000007DF24DF63EB.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.2MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/1642F168-E208-4E22-A5B1-F99B8D2B2F0F-8712-000007DE9F8A4D07.aac">1642F168-E208-4E22-A5B1-F99B8D2B2F0F-8712-000007DE9F8A4D07.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.18MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/DEBE0DB2-ADF1-4930-9AD7-F4AB365E0D91-8712-000007DE4751EBC8.aac">DEBE0DB2-ADF1-4930-9AD7-F4AB365E0D91-8712-000007DE4751EBC8.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.22MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/03658128-2787-46E1-BD09-0F069C254862-8712-000007DD9A2E8F65.aac">03658128-2787-46E1-BD09-0F069C254862-8712-000007DD9A2E8F65.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.14MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/E022570E-32B0-41F1-81A8-6273CF80451B-8712-000007DCBD7C7D0B.aac">E022570E-32B0-41F1-81A8-6273CF80451B-8712-000007DCBD7C7D0B.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.21MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/98333076-0628-4435-AB23-7FE40735A13B-8712-000007DC41C8DB1C.aac">98333076-0628-4435-AB23-7FE40735A13B-8712-000007DC41C8DB1C.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.19MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/481421C1-D8FB-4D48-94A1-E2CF4D188B9F-8712-000007DBE238ACC3.aac">481421C1-D8FB-4D48-94A1-E2CF4D188B9F-8712-000007DBE238ACC3.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.17MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/E5360DD1-B7D3-4F16-9B50-CCE4EF1F7DA9-8712-000007DB0EFDB79B.aac">E5360DD1-B7D3-4F16-9B50-CCE4EF1F7DA9-8712-000007DB0EFDB79B.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.19MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/0DA18FA4-0D27-41C5-BA43-F672EDDCC874-8712-000007DAC1B75329.aac">0DA18FA4-0D27-41C5-BA43-F672EDDCC874-8712-000007DAC1B75329.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.17MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/6930E984-68FF-4BF2-8D5F-76A849976E65-8712-000007D9B5924378.aac">6930E984-68FF-4BF2-8D5F-76A849976E65-8712-000007D9B5924378.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.14MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/E58153CC-E6CD-420F-A355-220A9D688D0B-8712-000007D9572736A2.aac">E58153CC-E6CD-420F-A355-220A9D688D0B-8712-000007D9572736A2.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.22MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/CD14EB1F-3E28-4FC6-A28F-F68DB3D39859-8712-000007D85B458717.aac">CD14EB1F-3E28-4FC6-A28F-F68DB3D39859-8712-000007D85B458717.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.21MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/A7B89BD3-31FE-4AA8-AF4E-3BB8E8CB98BD-8712-000007D7AA5A523F.aac">A7B89BD3-31FE-4AA8-AF4E-3BB8E8CB98BD-8712-000007D7AA5A523F.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.22MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/742A622A-415F-4250-A354-492284BA91A9-8712-000007D72B134F9B.aac">742A622A-415F-4250-A354-492284BA91A9-8712-000007D72B134F9B.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.19MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/AA23B098-C680-4204-90AE-1ADACA3AB846-8712-000007D6D355726A.aac">AA23B098-C680-4204-90AE-1ADACA3AB846-8712-000007D6D355726A.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.19MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/E27FFC05-5E81-4F1D-A37C-61E04A6C4C58-8712-000007D5E9F407FA.aac">E27FFC05-5E81-4F1D-A37C-61E04A6C4C58-8712-000007D5E9F407FA.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.21MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/8ECD52DE-009F-4E33-9AAA-399581620503-8712-000007D58B82AA05.aac">8ECD52DE-009F-4E33-9AAA-399581620503-8712-000007D58B82AA05.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.21MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/6B7F54FB-A338-4BBF-BF4F-E1DC8AA40D57-8712-000007D53869F5A4.aac">6B7F54FB-A338-4BBF-BF4F-E1DC8AA40D57-8712-000007D53869F5A4.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.17MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div><div class="download_item">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url" href="https://media.qlchat.com/wtLive/audio/12CE53E4-1DCD-4648-8595-BC5BBEFDA110-8712-000007D4E9BB0319.aac">12CE53E4-1DCD-4648-8595-BC5BBEFDA110-8712-000007D4E9BB0319.aac</a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="#">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size">0.22MB</div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div></div>
		
				<div class="download_item" id="download_item_template">
				  <div class="info">
					<div class="leftContent">					
						<div class="download_quality">
							<div class="media_quality"></div>
							<div class="media_format"><img></div>
						</div>					
						<a class="download_url"></a>				
					</div>	
				
					<div class="buttonsSmall">
						<a title="复制到剪贴板" class="copyLink"></a>	
						<a title="从列表中删除" class="removeLink"></a>						
					</div>

					<div class="rightContent">								
						<a class="download_button" href="">
						  <span class="text">下载</span>
						  <div class="loading"></div>
						  <div class="size"></div>
						</a>
					</div>
				  </div>
				  <div class="line"></div>	
					
				</div>
			</div>

			<div id="empty_download_block" hidden="true">
				<h2 id="empty_download_block_title">找不到媒体下载。</h2>
			</div>
		</div>
	</div>
	
	<div id="help_padding_block"></div>
	<!-- <div id="help_block">		
		<div class="bgLine"></div>
	</div> -->

</body>'''
soup = BeautifulSoup(voicesHtml,'html.parser')
for voiceUrl in soup.select('.download_url'):
    print(voiceUrl['href'])