"""
Module: In-Browser Screen Recorder Studio
Student Assessment: Problem P10
Subject: Generative AI

Provides a lightweight, zero-dependency in-browser screen recorder widget using
the HTML5 MediaStream and MediaRecorder API. Allows recording, previewing,
and downloading the 2-3 minute demo video directly from the application interface.
"""

import streamlit as st
import streamlit.components.v1 as components


def render_screen_recorder(theme: str = "dark") -> None:
    """Renders the HTML5 in-browser screen recorder and demo teleprompter."""
    is_dark = "light" not in theme.lower()
    
    bg_card = "#0F172A" if is_dark else "#FFFFFF"
    border_color = "#1E293B" if is_dark else "#E2E8F0"
    text_primary = "#F8FAFC" if is_dark else "#0F172A"
    text_secondary = "#94A3B8" if is_dark else "#64748B"
    cue_bg = "#1E293B" if is_dark else "#F1F5F9"
    
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            * {
                box-sizing: border-box;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            }
            body {
                margin: 0;
                padding: 12px;
                background: transparent;
                color: __TEXT_PRIMARY__;
            }
            .recorder-container {
                background: __BG_CARD__;
                border: 1px solid __BORDER_COLOR__;
                border-radius: 12px;
                padding: 16px 20px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            }
            .rec-header {
                display: flex;
                align-items: center;
                justify-content: space-between;
                margin-bottom: 14px;
            }
            .rec-title-group {
                display: flex;
                align-items: center;
                gap: 8px;
            }
            .rec-title {
                font-size: 1.05rem;
                font-weight: 700;
                margin: 0;
                color: __TEXT_PRIMARY__;
            }
            .badge-live {
                display: none;
                align-items: center;
                gap: 6px;
                background: rgba(239, 68, 68, 0.15);
                border: 1px solid rgba(239, 68, 68, 0.4);
                color: #EF4444;
                padding: 3px 8px;
                border-radius: 6px;
                font-size: 0.72rem;
                font-weight: 700;
                letter-spacing: 0.05em;
                text-transform: uppercase;
            }
            .badge-live.active {
                display: flex;
            }
            .pulse-dot {
                width: 8px;
                height: 8px;
                background: #EF4444;
                border-radius: 50%;
                animation: pulse 1s infinite;
            }
            @keyframes pulse {
                0% { opacity: 1; }
                50% { opacity: 0.3; }
                100% { opacity: 1; }
            }
            .timer-display {
                font-family: monospace;
                font-size: 1.25rem;
                font-weight: 700;
                color: #38BDF8;
                background: __CUE_BG__;
                padding: 4px 12px;
                border-radius: 6px;
                border: 1px solid __BORDER_COLOR__;
            }
            .btn-row {
                display: flex;
                gap: 10px;
                align-items: center;
                margin-bottom: 14px;
            }
            button {
                cursor: pointer;
                font-size: 0.82rem;
                font-weight: 600;
                border-radius: 8px;
                padding: 8px 16px;
                border: none;
                transition: all 0.2s ease;
                display: flex;
                align-items: center;
                gap: 6px;
            }
            .btn-start {
                background: linear-gradient(135deg, #EF4444 0%, #DC2626 100%);
                color: white;
                box-shadow: 0 2px 8px rgba(239, 68, 68, 0.3);
            }
            .btn-start:hover {
                transform: translateY(-1px);
                box-shadow: 0 4px 12px rgba(239, 68, 68, 0.4);
            }
            .btn-stop {
                background: #334155;
                color: #F8FAFC;
                border: 1px solid #475569;
            }
            .btn-stop:hover {
                background: #475569;
            }
            .btn-download {
                background: linear-gradient(135deg, #10B981 0%, #059669 100%);
                color: white;
                display: none;
                box-shadow: 0 2px 8px rgba(16, 185, 129, 0.3);
            }
            .btn-download:hover {
                transform: translateY(-1px);
                box-shadow: 0 4px 12px rgba(16, 185, 129, 0.4);
            }
            .preview-container {
                display: none;
                margin-top: 12px;
                border-top: 1px solid __BORDER_COLOR__;
                padding-top: 12px;
            }
            video {
                width: 100%;
                max-height: 240px;
                border-radius: 8px;
                background: black;
                border: 1px solid __BORDER_COLOR__;
            }
            .teleprompter-box {
                margin-top: 10px;
                background: __CUE_BG__;
                border: 1px solid __BORDER_COLOR__;
                border-radius: 8px;
                padding: 10px 14px;
                font-size: 0.78rem;
                color: __TEXT_SECONDARY__;
                line-height: 1.5;
            }
            .cue-highlight {
                color: #818CF8;
                font-weight: 700;
            }
        </style>
    </head>
    <body>
        <div class="recorder-container">
            <div class="rec-header">
                <div class="rec-title-group">
                    <span style="font-size: 1.2rem;">📹</span>
                    <h3 class="rec-title">Demo Video Screen Recorder</h3>
                    <div id="liveBadge" class="badge-live">
                        <div class="pulse-dot"></div>
                        <span>RECORDING</span>
                    </div>
                </div>
                <div id="timer" class="timer-display">00:00 / 02:30</div>
            </div>

            <div class="btn-row">
                <button id="startBtn" class="btn-start" onclick="startRecording()">
                    <span>🔴</span> Start Screen Recording
                </button>
                <button id="stopBtn" class="btn-stop" onclick="stopRecording()" disabled>
                    <span>⏹️</span> Stop Recording
                </button>
                <button id="downloadBtn" class="btn-download" onclick="downloadVideo()">
                    <span>⬇️</span> Download Video (Demo_Recording_P10.webm)
                </button>
            </div>

            <div class="teleprompter-box">
                <b>🎬 2-Min Demo Script Cue:</b> 
                <span class="cue-highlight">[0:00]</span> Platform Overview &bull;
                <span class="cue-highlight">[0:20]</span> Health Score &bull;
                <span class="cue-highlight">[0:40]</span> Distributions &amp; ML Rec &bull;
                <span class="cue-highlight">[1:00]</span> AST-Safe Query &bull;
                <span class="cue-highlight">[1:25]</span> S-BERT &amp; Vision &bull;
                <span class="cue-highlight">[1:45]</span> PyTorch CTGAN &bull;
                <span class="cue-highlight">[2:05]</span> Responsible AI PII &bull;
                <span class="cue-highlight">[2:20]</span> PDF Report Download
            </div>

            <div id="previewArea" class="preview-container">
                <div style="font-size: 0.8rem; font-weight: 600; color: __TEXT_PRIMARY__; margin-bottom: 6px;">
                    Preview Recorded Demonstration:
                </div>
                <video id="videoPreview" controls></video>
            </div>
        </div>

        <script>
            let mediaRecorder;
            let recordedChunks = [];
            let stream = null;
            let timerInterval = null;
            let seconds = 0;
            let recordedBlob = null;

            async function startRecording() {
                try {
                    stream = await navigator.mediaDevices.getDisplayMedia({
                        video: { cursor: "always" },
                        audio: true
                    });

                    recordedChunks = [];
                    mediaRecorder = new MediaRecorder(stream, { mimeType: 'video/webm;codecs=vp9,opus' });

                    mediaRecorder.ondataavailable = function(e) {
                        if (e.data.size > 0) {
                            recordedChunks.push(e.data);
                        }
                    };

                    mediaRecorder.onstop = function() {
                        recordedBlob = new Blob(recordedChunks, { type: 'video/webm' });
                        const videoURL = URL.createObjectURL(recordedBlob);
                        const preview = document.getElementById('videoPreview');
                        preview.src = videoURL;
                        document.getElementById('previewArea').style.display = 'block';
                        document.getElementById('downloadBtn').style.display = 'inline-flex';
                        
                        clearInterval(timerInterval);
                        document.getElementById('liveBadge').classList.remove('active');
                        document.getElementById('startBtn').disabled = false;
                        document.getElementById('stopBtn').disabled = true;
                    };

                    // Handle user clicking native browser "Stop sharing" bar
                    stream.getVideoTracks()[0].onended = function() {
                        if (mediaRecorder && mediaRecorder.state !== 'inactive') {
                            stopRecording();
                        }
                    };

                    mediaRecorder.start(250); // grab chunks every 250ms
                    
                    document.getElementById('startBtn').disabled = true;
                    document.getElementById('stopBtn').disabled = false;
                    document.getElementById('liveBadge').classList.add('active');
                    document.getElementById('previewArea').style.display = 'none';
                    document.getElementById('downloadBtn').style.display = 'none';

                    seconds = 0;
                    clearInterval(timerInterval);
                    timerInterval = setInterval(() => {
                        seconds++;
                        let mins = String(Math.floor(seconds / 60)).padStart(2, '0');
                        let secs = String(seconds % 60).padStart(2, '0');
                        document.getElementById('timer').innerText = mins + ":" + secs + " / 02:30";
                        if (seconds >= 150) {
                            document.getElementById('timer').style.color = '#EF4444';
                        }
                    }, 1000);

                } catch (err) {
                    console.error("Screen capture error:", err);
                    alert("Screen capture was canceled or not supported by this browser.");
                }
            }

            function stopRecording() {
                if (mediaRecorder && mediaRecorder.state !== 'inactive') {
                    mediaRecorder.stop();
                    if (stream) {
                        stream.getTracks().forEach(track => track.stop());
                    }
                }
            }

            function downloadVideo() {
                if (!recordedBlob) return;
                const a = document.createElement('a');
                a.style.display = 'none';
                a.href = URL.createObjectURL(recordedBlob);
                a.download = 'Demo_Recording_P10.webm';
                document.body.appendChild(a);
                a.click();
                setTimeout(() => {
                    document.body.removeChild(a);
                    window.URL.revokeObjectURL(a.href);
                }, 100);
            }
        </script>
    </body>
    </html>
    """
    
    recorder_html = (
        html_template
        .replace("__BG_CARD__", bg_card)
        .replace("__BORDER_COLOR__", border_color)
        .replace("__TEXT_PRIMARY__", text_primary)
        .replace("__TEXT_SECONDARY__", text_secondary)
        .replace("__CUE_BG__", cue_bg)
    )
    
    components.html(recorder_html, height=270, scrolling=False)
